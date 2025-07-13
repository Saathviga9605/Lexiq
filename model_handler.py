import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}


MODEL_ENDPOINTS = {
    "mistral": "mistralai/mistral-7b-instruct",
    "mixtral": "mistralai/mixtral-8x7b-instruct"
}


def count_tokens(text: str) -> int:
    return len(text.split())
def get_model_response(prompt: str, model: str):
    model_id = MODEL_ENDPOINTS.get(model)
    
    if not model_id:
        return "Invalid model selected.", 0

    payload = {
        "model": model_id,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    start_time = time.time()
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload
    )
    latency = round((time.time() - start_time) * 1000)

    if response.status_code != 200:
        print(" API ERROR ")
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        return "Error from OpenRouter API", 0

    try:
        data = response.json()
        message = data["choices"][0]["message"]["content"]
        token_count = count_tokens(message)
        return message, token_count
    except Exception as e:
        return f"Response parse error: {e}", 0
