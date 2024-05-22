import json
import sys
from neo4j import GraphDatabase

uri = "bolt://localhost:31001"
username = "neo4j"
password = "password"

driver = GraphDatabase.driver(uri, auth=(username, password))

def import_data(tx, data):
    for obj in data['objects']:
        obj_type = obj['type']
        obj_id = obj['id']
        
        if obj_type == "process":
            tx.run(
                "MERGE (p:Process {id: $id, pid: $pid, command_line: $command_line, cwd: $cwd, created_time: $created_time}) "
                "WITH p "
                "MATCH (f:File {id: $image_ref}) "
                "MERGE (p)-[:USES_IMAGE]->(f) ",
                id=obj_id, pid=obj['pid'], command_line=obj['command_line'], cwd=obj['cwd'], created_time=obj['created_time'], image_ref=obj['image_ref']
            )
            if 'parent_ref' in obj:
                tx.run(
                    "MATCH (p:Process {id: $id}), (parent:Process {id: $parent_id}) "
                    "MERGE (parent)-[:SPAWNED]->(p) ",
                    id=obj_id, parent_id=obj['parent_ref']
                )
                
        elif obj_type == "file":
            tx.run(
                "MERGE (f:File {id: $id, name: $name}) ",
                id=obj_id, name=obj['name']
            )
            
        elif obj_type == "observed-data":
            tx.run(
                "MERGE (o:ObservedData {id: $id, created: $created, modified: $modified, first_observed: $first_observed, last_observed: $last_observed, number_observed: $number_observed}) ",
                id=obj_id, created=obj['created'], modified=obj['modified'], first_observed=obj['first_observed'], last_observed=obj['last_observed'], number_observed=obj['number_observed']
            )
            for ref in obj['object_refs']:
                tx.run(
                    "MATCH (o:ObservedData {id: $obs_id}), (ref {id: $ref_id}) "
                    "MERGE (o)-[:OBSERVED]->(ref) ",
                    obs_id=obj_id, ref_id=ref
                )
                
        elif obj_type == "attack-pattern":
            tx.run(
                "MERGE (a:AttackPattern {id: $id, name: $name, description: $description}) ",
                id=obj_id, name=obj['name'], description=obj['description']
            )
            
        elif obj_type == "intrusion-set":
            tx.run(
                "MERGE (i:IntrusionSet {id: $id, name: $name, description: $description, goals: $goals}) ",
                id=obj_id, name=obj['name'], description=obj['description'], goals=obj['goals']
            )
            
        elif obj_type == "indicator":
            tx.run(
                "MERGE (i:Indicator {id: $id, name: $name, description: $description, pattern: $pattern, pattern_type: $pattern_type, valid_from: $valid_from}) ",
                id=obj_id, name=obj['name'], description=obj['description'], pattern=obj['pattern'], pattern_type=obj['pattern_type'], valid_from=obj['valid_from']
            )
            
        elif obj_type == "relationship":
            rel_type = obj['relationship_type']
            source_ref = obj['source_ref']
            target_ref = obj['target_ref']
            tx.run(
                f"MATCH (s {{id: $source_ref}}), (t {{id: $target_ref}}) "
                f"MERGE (s)-[:{rel_type.upper().replace('-', '_')}]->(t) ",
                source_ref=source_ref, target_ref=target_ref
            )

def main(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    with driver.session() as session:
        session.execute_write(import_data, data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_json_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    main(file_path)