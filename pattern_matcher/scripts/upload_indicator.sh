#!/bin/bash
#
# This script uploads indicators and other STIX Domain Objects into
# neo4j running in kubernetes

STIX_MODEL_PATH=$1
POD_NAME=$(kubectl get pods -n redpanda -l app=matcher -o jsonpath='{.items[0].metadata.name}')
kubectl cp "${STIX_MODEL_PATH}" redpanda/"${POD_NAME}":/tmp
kubectl exec -it -n redpanda "${POD_NAME}" -- python -m patternmatcher.load "/tmp/$(basename ${STIX_MODEL_PATH})"

# Query for matches in Neo4j
# MATCH p=(:Indicator)-[:MATCHED]->(:ObservedData)-[:OBSERVED]->() RETURN p
