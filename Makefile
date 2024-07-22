STIX_MODEL_PATH=stix/examples/stix-attack-model.json

all:  install-neo4j install-matcher insert-attack-models

install-neo4j:
	helm repo add neo4j https://helm.neo4j.com/neo4j
	helm repo update
	helm upgrade --install --create-namespace neo4j-poc neo4j/neo4j --namespace neo4j -f neo4j/values.yaml
	kubectl -n neo4j wait --timeout=10m --for=condition=Ready pod -l app=hub

install-matcher:
	kubectl apply -f pattern_matcher/resources.yaml
	kubectl -n redpanda wait --for=condition=Ready pod -l app=matcher

forward-neo4j:
	kubectl port-forward -n neo4j service/neo4j-poc 7474:7474 &
	kubectl port-forward -n neo4j service/neo4j-poc 7687:7687

insert-attack-models:
	POD_NAME=$$(kubectl get pods -n redpanda -l app=matcher -o jsonpath='{.items[0].metadata.name}') ;\
	kubectl cp ${STIX_MODEL_PATH} redpanda/$${POD_NAME}:/tmp ;\
	kubectl exec -it -n redpanda $${POD_NAME} -- python /app/src/patternmatcher/load.py /tmp/$(notdir ${STIX_MODEL_PATH})

destroy: destroy-matcher destroy-neo4j

destroy-matcher:
	kubectl delete deployment/matcher -n redpanda

destroy-neo4j:
	helm uninstall neo4j-poc -n neo4j
	kubectl delete ns neo4j
