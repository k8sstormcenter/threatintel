---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.4
  kernelspec:
    display_name: .venv
    language: python
    name: python3
---

# LLM exploration for Threat Intelligence
This notebook creates some exploration, how LLMs can be utilized to support users when analyzing STIX Domain Objects.

```python
import os
import json

import google.generativeai as genai
from google.generativeai.generative_models import GenerativeModel
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
print("set") if GOOGLE_API_KEY else print("unset")
genai.configure(api_key=GOOGLE_API_KEY)
```

```python
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
```

```python
from kscLLM.util import to_markdown, get_model

model = get_model()
```

```python
%%time
response = model.generate_content("What is STIX?")
```


```python
to_markdown(response.text)
# print(response.text)
```


```python
# observables_bundle = {
#     "type": "bundle",
#     "id": "bundle--9896add8-7ede-4bca-83c4-40b06174436d",
#     "spec_version": "2.1",
#     "objects": [
#       {
#         "type": "file",
#         "id": "file--59f1fbaf-42e2-43c1-888f-12fab5ee119c",
#         "name": "containerd-shim-runc-v2"
#       },
#       {
#         "type": "file",
#         "id": "file--939d4535-e6a8-4cd2-8d2f-f22dc4e2b76b",
#         "name": "nsenter"
#       },
#       {
#         "type": "process",
#         "id": "process--dac3607d-92ff-4021-ae7c-53d87322f1dd",
#         "pid": 77047,
#         "command_line": "/usr/local/bin/containerd-shim-runc-v2 -namespace k8s.io -id 5dffbff9c65c9d05e03717f331c0d4341c4d4748068bec14f865f865a46a6dec -address /run/containerd/containerd.sock",
#         "cwd": "/run/containerd/io.containerd.runtime.v2.task/k8s.io/5dffbff9c65c9d05e03717f331c0d4341c4d4748068bec14f865f865a46a6dec",
#         "created_time": "2024-08-20T19:31:24.445163755Z",
#         "image_ref": "file--59f1fbaf-42e2-43c1-888f-12fab5ee119c",
#         "extensions": {
#           "flags": "execve clone",
#           "parent_exec_id": "aG9uZXljbHVzdGVyLWNvbnRyb2wtcGxhbmU6NDQ4NjU3ODk5MzQ2OTo3NzA0MA=="
#         }
#       },
#       {
#         "type": "process",
#         "id": "process--1b39957a-1f9b-4df1-8917-4ec955c73e66",
#         "pid": 77148,
#         "command_line": "/usr/bin/nsenter --mount=/proc/1/ns/mnt -- /bin/bash",
#         "cwd": "/",
#         "created_time": "2024-08-20T19:31:29.510044941Z",
#         "image_ref": "file--939d4535-e6a8-4cd2-8d2f-f22dc4e2b76b",
#         "parent_ref": "process--dac3607d-92ff-4021-ae7c-53d87322f1dd",
#         "extensions": {
#           "flags": "execve rootcwd clone",
#           "docker": "b61d19d405d15e303fe8fc5c7bc64d2",
#           "container_id": "containerd://b61d19d405d15e303fe8fc5c7bc64d2ae0317a52cc22761d9cd986bb4a254694",
#           "pod_name": "atomic-nsenter-escape-pod",
#           "namespace": "default"
#         }
#       },
#       {
#         "type": "observed-data",
#         "id": "observed-data--ed1f2ade-0fe9-43f1-ac23-acfe38eb2893",
#         "created": "2024-08-23T11:38:57.016347Z",
#         "modified": "2024-08-23T11:38:57.016347Z",
#         "first_observed": "2024-08-23T11:38:57.016347Z",
#         "last_observed": "2024-08-23T11:38:57.016347Z",
#         "number_observed": 1,
#         "object_refs": [
#           "process--1b39957a-1f9b-4df1-8917-4ec955c73e66",
#           "process--dac3607d-92ff-4021-ae7c-53d87322f1dd",
#           "file--59f1fbaf-42e2-43c1-888f-12fab5ee119c",
#           "file--939d4535-e6a8-4cd2-8d2f-f22dc4e2b76b"
#         ],
#         "extensions": {
#           "node_info": {
#             "node_name": None
#           }
#         }
#c      }
#     ]
#   }

# from rag.index import ROOT_PATH
# print(ROOT_PATH)


```


```python
with open("../../pattern_matcher/resource/stix/observed/oss/positives_token_theft.json", "r") as file:
    observables_bundle = json.load(file)

prompt = f"""{str(observables_bundle)}"""


response_indicator = model.generate_content(prompt)
to_markdown(response_indicator.text)
```






```python
prompt = f"""Check the following observables for suspicious activity. Report whether such activity occured and describe the attack if one is present.

{observables_bundle}"""
to_markdown(model.generate_content(prompt).text)
```

```python

prompt = f"""Check the following observables for suspicious activity. Report whether such activity occured, don't provide indicators.

{observables_bundle}"""
to_markdown(model.generate_content(prompt).text)
```

## Only return STIX

```python
prompt_only_stix = f"""Create STIX indicators to match the following observables. Only provide the json.
{observables_bundle}
"""
res = model.generate_content(prompt_only_stix)
print(res.text)
```


# Produce patterns for a well known attack

```python
prompt_peirates = """Create STIX indicators to match the installation of peirates. Only provide the json."""

res = model.generate_content(prompt_peirates)
```


```python
print(res.text)
# res.text
```

```python
with open("../../pattern_matcher/resource/stix/observed/MITRE/T1611/T1611-nsenter_observed.json", "r") as file:
    complete_attack = json.load(file)

prompt_complete_attack = f"""Create a STIX bundle including indicator and attack pattern to match the following attack:

{complete_attack}
"""

res = model.generate_content(prompt_complete_attack)
```


```python
print(res.text)
```
