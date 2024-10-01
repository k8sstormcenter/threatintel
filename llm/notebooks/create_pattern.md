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

from google.generativeai.generative_models import GenerativeModel
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
print("set") if GOOGLE_API_KEY else print("unset")
```

```python
import google.generativeai as genai
genai.configure(api_key=GOOGLE_API_KEY)


for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
```

```python
from IPython.display import Markdown, display
import textwrap

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
```


```python
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]
model = genai.GenerativeModel(
    'gemini-1.5-pro', 
    safety_settings=safety_settings, 
    generation_config=genai.GenerationConfig(
        temperature=0.9
    ),
    system_instruction="""You are a cybersecurity expert specializing in STIX. You will be provided with STIX 2.1 observables describing potential cyberattacks. Your task is to create corresponding **valid and accurate STIX 2.1 indicators** that effectively detect and characterize these attacks. 

Focus on crafting indicators that are:

* **Specific:** Precisely matching the provided observables.
* **Actionable:** Usable by security tools for detection and response.
* **Context-rich:** Including relevant pattern details, attack motivations, and potential impact.

""",
)
```



```python
with open("../../pattern_matcher/resource/stix/observed/oss/positives_token_theft.json", "r") as file:
    observables_bundle = json.load(file)

prompt = f"""{str(observables_bundle)}"""


response_indicator = model.generate_content(prompt)
to_markdown(response_indicator.text)
```



