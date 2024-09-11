#!/bin/bash

kubectl delete -n redpanda deployments.apps matcher
poetry build
docker build -t local/matcher:latest .
kind load docker-image local/matcher:latest --name honeycluster
kubectl apply -f resources.yaml


