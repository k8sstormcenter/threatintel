#!/bin/bash

APPLOG_LOCATION=$1
STIX_PATH=$2
TMP_DIR=$(mktemp -d "/tmp/patternmatcher.XXXXXXXXXXXXX")
PREPROCESSED="${TMP_DIR}/pre.json"
# SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

kubectl exec -it -n redpanda redpanda-src-0 -- rpk topic consume applogs --offset @-10m:end -f '%v\n' > "$APPLOG_LOCATION"

# convert applog to STIX format
jq -s "." < "$APPLOG_LOCATION" > "$PREPROCESSED" # loaded from rpk
python -m patternmatcher.parse "$PREPROCESSED" > "$STIX_PATH"

# will load STIX file into neo4j
# python -m patternmatcher.load "$STIX_PATH"
