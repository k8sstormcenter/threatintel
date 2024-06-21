all: install-matcher install-neo4j insert-attack-models

install-matcher:
	kubectl apply -f pattern_matcher/resources.yaml

install-neo4j:
	helm repo add neo4j https://helm.neo4j.com/neo4j
	helm repo update
	helm upgrade --install --create-namespace neo4j-poc neo4j/neo4j --namespace neo4j -f neo4j/values.yaml

forward-neo4j:
	kubectl port-forward -n neo4j service/neo4j-poc 7687:7687

# For now, needs patternmatcher package installed in active python virtual environment
# and port-forwarding of neo4j using forward-neo4j rule
insert-attack-models:
	kubectl cp stix/code/stix-attack-tree.json redpanda/matcher:/tmp/.
	kubectl cp pattern_matcher/src/patternmatcher/load.py redpanda/matcher:/app/src/patternmatcher/load.py
	kubectl exec -it -n redpanda matcher -- python /app/src/patternmatcher/load.py /tmp/stix-attack-tree.json



destroy-matcher:
	kubectl delete pods matcher -n redpanda

destroy-neo4j:
	helm uninstall neo4-poc -n neo4j
	kubectl delete ns neo4j
