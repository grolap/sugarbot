from dotenv import load_dotenv
import os

load_dotenv()

# Telegram Bot
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# SUGAR AI API
SUGAR_AI_API = os.environ.get("SUGAR_AI_API")

# APP
APP_URL = os.environ.get("APP_URL")
