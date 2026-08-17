import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2",
        "prompt": "Explain what a dashboard is in two sentences.",
        "stream": False
    }
)

response.raise_for_status()

print(response.json()["response"])