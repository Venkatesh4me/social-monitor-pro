from dotenv import load_dotenv
load_dotenv()

import json
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

WEBSITES_FILE = "app/config/websites.json"
STATE_FILE = "state/state.json"

def load_websites():
    with open(WEBSITES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)