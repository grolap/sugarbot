import requests

import json

from urllib3 import HTTPConnectionPool

from services.config import SUGAR_AI_API


def get_answer(message: str):
    headers = {"Content-Type": "application/json"}
    data = {"query": message}

    data = json.dumps(data)
    while True:
        try:
            response = requests.post(SUGAR_AI_API, headers=headers, data=data, timeout=20)
            return response.json()["content"]
        except requests.exceptions.Timeout:
            return "Сегодня я уже устал и не готов с Вами общаться..."
