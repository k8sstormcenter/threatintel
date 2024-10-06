#!/bin/bash

# STIX_PATH=$1
TMP_DIR=$(mktemp -d "/tmp/patternmatcher.XXXXXXXXXXXXX")
REDPANDA_LOCATION="$TMP_DIR/redpanda.json"
PREPROCESSED="${TMP_DIR}/pre.json"
# SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

kubectl exec -it -n redpanda redpanda-src-0 -- rpk topic consume applogs --offset @-10m:end -f '%v\n' > "$REDPANDA_LOCATION"

# convert applog to STIX format
jq -s "." < "$REDPANDA_LOCATION" > "$PREPROCESSED" # loaded from rpk
python -m patternmatcher.parse "$PREPROCESSED"     # > "$STIX_PATH"

# will load STIX file into neo4j
# python -m patternmatcher.load "$STIX_PATH"
