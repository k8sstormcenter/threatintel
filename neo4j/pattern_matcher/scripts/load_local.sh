#!/bin/bash
#
# This scripts loads a downloaded tetragon json file (e.g. downloaded
# from the redpanda UI) into neo4j.
# The patternmatcher package has to be installed in the active
# Python environment.

TETRAGON_LOG="$1"
STIX_PATH="tmp/stix.json"
PREPROCESSED="tmp/pre.json"

install -D /dev/null "$STIX_PATH"
install -D /dev/null "$PREPROCESSED"

# make json valid
sed -z 's#}\n{#},\n{#g' "$TETRAGON_LOG" > "$PREPROCESSED"
sed -i '1s#^#[#' "$PREPROCESSED"
echo -n "]" >> "$PREPROCESSED"

# map tetragon log to stix
python -m patternmatcher.parse "$PREPROCESSED" > "$STIX_PATH"

# load stix into neo4j
python -m patternmatcher.load "$STIX_PATH"

