import json
import os
from app.config import STATE_FILE


class StateManager:

    def __init__(self):
        self.state = self.load()

    def load(self):

        if not os.path.exists(STATE_FILE):
            return {
                "version": 1,
                "last_run": "",
                "total_articles_seen": 0,
                "websites": {}
            }

        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self):

        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=4)

    def has_seen(self, website, article_hash):

        if website not in self.state["websites"]:
            return False

        return article_hash in self.state["websites"][website]

    def add_article(self, website, article_hash):

        if website not in self.state["websites"]:
            self.state["websites"][website] = []

        self.state["websites"][website].append(article_hash)

        self.state["total_articles_seen"] += 1

        if len(self.state["websites"][website]) > 500:
            self.state["websites"][website] = self.state["websites"][website][-500:]