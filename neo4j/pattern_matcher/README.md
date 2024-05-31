# Pattern Matcher


## Usage

## Load a local log manually into neo4j:
Start a neo4j instance:

```bash
cd .. && docker compose up
```

Install the patternmatcher package in the current
python environment:
```bash
pip install .
```
Alternatively one could also use poetry:
```bash
poetry install
```

Load a tetragon log (e.g. from redpanda) into
the started neo4j instance:

Beware this script creates 2 files in ```$(pwd)/tmp```, one
 for the preprocessed tetragon logs (to make them valid json)
and one for the converted stix, which is uploaded to neo4j.
```bash
./scripts/load_local.sh /path/to/tetragon_log.json
```
