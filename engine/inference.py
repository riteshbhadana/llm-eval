import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
HEADERS = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

def run_model(prompt):

    payload = {"inputs": prompt}

    for _ in range(5):  # retry attempts
        response = requests.post(API_URL, headers=HEADERS, json=payload)

        if response.status_code == 200:
            data = response.json()
            return data[0]["generated_text"]

        elif response.status_code == 503:
            print("Model loading… retrying")
            time.sleep(5)

        else:
            print("HF Error:", response.text)
            break

    return "Model failed"
