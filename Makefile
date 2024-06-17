install-matcher:
	kubectl apply -f pattern_matcher/resources.yaml

install-neo4j:
	helm repo add neo4j https://helm.neo4j.com/neo4j
	helm repo update
	helm install --create-namespace neo4j-poc neo4j/neo4j --namespace neo4j -f values.yaml

forward-neo4j:
	kubectl port-forward -n neo4j service/neo4j-poc 7687:7687

# For now, needs patternmatcher package installed in active python virtual environment
# and port-forwarding of neo4j using forward-neo4j rule
insert-attack-models:
	python -m patternmatcher.load ./stix/code/stix-attack-tree.json


destroy-matcher:
	kubectl delete pods matcher -n redpanda

destroy-neo4j:
	helm uninstall neo4-poc -n neo4j
	kubectl delete ns neo4j
