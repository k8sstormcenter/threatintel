from datetime import datetime
import textwrap
import google.generativeai as genai

from IPython.display import Markdown, display
from google.generativeai.client import pathlib

from kscLLM.index import ROOT_PATH


def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


def get_model():
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

    with open(ROOT_PATH / "resource/stix_specification_plain.txt") as file:
        lines = file.readlines()
    system_prompt = "\n".join(lines)
    model = genai.GenerativeModel(
        "gemini-1.5-pro",
        safety_settings=safety_settings,
        generation_config=genai.GenerationConfig(temperature=0.9),
        system_instruction=f"""You are a cyber threat intelligence expert specializing in STIX. You will be provided with STIX 2.1 Domain Objects describing potential cyberattacks.

    Focus on crafting responses that are:

    * **Specific:** Precisely matching the provided observables.
    * **Actionable:** Usable by security tools for detection and response.
    * **Context-rich:** Including relevant pattern details, attack motivations, and potential impact.

    {system_prompt}
    """,
    )

    return model


def get_current_time() -> str:
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
