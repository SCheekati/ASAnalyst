# llm_analysis.py
import requests
import openai
from config import OPENAI_API_KEY
from ollama_config import OLLAMA_API_URL, OLLAMA_PROMPT_TEMPLATE
from openwebui_config import OPENWEBUI_API_URL, OPENWEBUI_PROMPT_TEMPLATE

def analyze_with_openai(data):
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": INITIAL_PROMPT},
            {"role": "user", "content": f"Analyze the following AS data:\n{json.dumps(data, indent=2)}"}
        ]
    )
    return response['choices'][0]['message']['content']

def analyze_with_ollama(data):
    payload = {
        "model": "internet_expert",
        "prompt": f"{OLLAMA_PROMPT_TEMPLATE}\n{json.dumps(data, indent=2)}"
    }
    response = requests.post(f"{OLLAMA_API_URL}/generate", json=payload)
    return response.json().get("generated", "")

def analyze_with_openwebui(data):
    payload = {
        "prompt": f"{OPENWEBUI_PROMPT_TEMPLATE}\n{json.dumps(data, indent=2)}",
        "model": "cybersecurity_expert"
    }
    response = requests.post(f"{OPENWEBUI_API_URL}/api/v1/generate", json=payload)
    return response.json().get("result", "")

def analyze_as_data(data, engine="openai"):
    if engine == "openai":
        return analyze_with_openai(data)
    elif engine == "ollama":
        return analyze_with_ollama(data)
    elif engine == "openwebui":
        return analyze_with_openwebui(data)
    else:
        raise ValueError("Unsupported engine selected.")
