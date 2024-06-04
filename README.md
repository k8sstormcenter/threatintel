# K8sStormCenter Threatintel
Collect tetragon logs from a honeycluster and transform them to STIX to load them into Neo4J.

## Structure
In the neo4j directory, the code to connect to a Kafka stream of Tetragon logs, convert that stream to STIX format and write the transformed objects to Neo4J is contained.

In the stix directory, attack trees in STIX format are collected as json files.


The conversion from Tetragon logs to STIX and uploading those logs to a Neo4J is done by [patternmatcher](./neo4j/pattern_matcher), which can be built and run using the provided [Dockerfile](./neo4j/pattern_matcher/Dockerfile).

## Getting started
To get started a running Neo4J instance is required, which will be used to upload the STIX logs to. Either run Neo4J directly on docker using the [docker compose](./neo4j/docker-compose.yaml) or deploy it to Kind / Kubernetes following this [setup](./neo4j/README.md).


In order to load data, the patternmatcher package needs to be installed by following this [setup](./neo4j/pattern_matcher/README.md).
Exported tetragon logs in json can be loaded using the local load [script](./neo4j/pattern_matcher/scripts/load_local.sh), which can be helpful when manually analyzing a single attack.

For the automated loading, the Kafka stream of Tetragon logs has to be forwarded to the patternmatcher Docker image (by default patternmatcher consumes from port 9093).
The patternmatcher uploads to Neo4J after transformation of the data (by default to port 7687).
Once both ports are forwarded for the machine running patternmatcher and patternmatcher is installed, it can be run by:

```bash
python -m patternmatcher.main --neo_uri <uri_to_neo4j> --kafka_uri <uri_to_kafka_stream>
```






