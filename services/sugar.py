import requests
import json
from services.config import SUGAR_AI_API


def get_answer(message: str):
    headers = {"Content-Type": "application/json"}
    data = {"query": message}

    data = json.dumps(data)
    while True:
        try:
            response = requests.post(SUGAR_AI_API, headers=headers, data=data)
            return response.json()["content"]
        except Exception as e:
            return str(e)
