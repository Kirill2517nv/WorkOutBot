import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
DB_PATH = os.getenv("DB_PATH", "workout.db")
PROXY_URL = os.getenv("PROXY_URL", "")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не задан в .env")
