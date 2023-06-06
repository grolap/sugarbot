import requests

import json

from services.messages import BOT_MESSAGES
from services.config import SUGAR_AI_API, TIMEOUT_API


def get_answer(message: str):
    url = f"{SUGAR_AI_API}/predict"
    headers = {"Content-Type": "application/json"}
    data = {"query": message}

    data = json.dumps(data)
    while True:
        try:
            response = requests.post(url=url, headers=headers, data=data, timeout=TIMEOUT_API)
            return response.json()["content"]
        except requests.exceptions.Timeout:
            return BOT_MESSAGES["timeout"]


def insert_answer(message: str):
    url = f"{SUGAR_AI_API}/insert"
    headers = {"Content-Type": "application/json"}
    data = {"content": message}

    data = json.dumps(data)
    while True:
        try:
            response = requests.post(url=url, headers=headers, data=data, timeout=20)
            if response.status_code == 200:
                return BOT_MESSAGES["insert_ok"]
            else:
                return BOT_MESSAGES["insert_error"]
        except requests.exceptions.Timeout:
            return BOT_MESSAGES["timeout"]
