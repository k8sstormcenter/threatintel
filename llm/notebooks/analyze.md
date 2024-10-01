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


```python
import os
import json
import google.generativeai as genai


GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
print("set") if GOOGLE_API_KEY else print("unset")
genai.configure(api_key=GOOGLE_API_KEY)
```


```python
from kscLLM.util import to_markdown, get_model
model = get_model()
```


# Load collected logs

```python
# ../../pattern_matcher/resource/stix/observed/oss/positives_token_theft.json
with open("../tmp/logs.json", "r") as file:
    observables_bundle = json.load(file)

prompt = f"""Report malicious activity in the following STIX Domain Objects. Respond by showing the malicious SDOs and a short description of why they are malicious. 
A credential access attack is searched. First a token is fetched. This token is then extracted by an SSRF attack which calls the google.internal service accounts token endpoint.
Find for each step of this attack the observable.

{str(observables_bundle)}"""


response_indicator = model.generate_content(prompt)
# to_markdown(response_indicator.text)
print(response_indicator.text)
```
