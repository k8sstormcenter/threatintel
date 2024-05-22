# STIX 2.1 to Neo4j POC

## Set up a Kind Cluster and Deploy Neo4j

Create a kind cluster:

```bash
kind create cluster
```

Deploy Neo4j:

```bash
helm repo add neo4j https://helm.neo4j.com/neo4j
helm repo update
kubectl create namespace neo4j
helm install neo4j-poc neo4j/neo4j --namespace neo4j -f values.yaml
```

Set up port forwarding:

```bash
kubectl port-forward service/hub-lb-neo4j -n neo4j 31000:7474 &
kubectl port-forward service/neo4j-poc -n neo4j 31001:7687 &
kubectl port-forward service/neo4j-poc-admin -n neo4j 31002:7687 &
```

Set up a python venv:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the `neo4j` Python driver:

```bash
pip3 install neo4j
```

Run the import script:

```bash
python3 load-stix-data.py ../stix/code/stix-attack-tree.json
python3 load-stix-data.py ../stix/code/stix-tetragon-log.json
```

Navigate to `http://localhost:31000/` to visualise the data, using the password `password` for the `neo4j` user.

## Teardown

```bash
kind delete cluster
```
