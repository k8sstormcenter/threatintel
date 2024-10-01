#!/bin/bash

APPLOG_LOCATION="tmp/applogs.json"
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

kubectl exec -it -n redpanda redpanda-src-0 -- rpk topic consume applogs --offset :end -f '%v\n' > $APPLOG_LOCATION

"$SCRIPT_DIR"/load_local.sh $APPLOG_LOCATION
