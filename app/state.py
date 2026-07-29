import json
import os
from datetime import datetime
from app.config import STATE_FILE


class StateManager:

    def __init__(self):
        self.state = self.load()

    def load(self):
        """Load state.json or create a default state."""

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
        """Save the current state to state.json."""

        self.state["last_run"] = datetime.utcnow().isoformat() + "Z"

        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=4)

    def has_seen(self, website: str, article_hash: str) -> bool:
        """Return True if this article has already been processed."""

        if website not in self.state["websites"]:
            return False

        return article_hash in self.state["websites"][website]

    def add_article(self, website: str, article_hash: str):
        """Add a newly discovered article hash."""

        if website not in self.state["websites"]:
            self.state["websites"][website] = []

        # Avoid duplicate hashes
        if article_hash not in self.state["websites"][website]:
            self.state["websites"][website].append(article_hash)
            self.state["total_articles_seen"] += 1

        # Keep only the latest 500 hashes per website
        self.state["websites"][website] = self.state["websites"][website][-500:]

    def get_total_articles(self) -> int:
        """Return the total number of stored article hashes."""
        return self.state["total_articles_seen"]

    def clear_website(self, website: str):
        """Clear stored hashes for a specific website."""

        if website in self.state["websites"]:
            del self.state["websites"][website]

    def clear_all(self):
        """Reset the complete monitoring state."""

        self.state = {
            "version": 1,
            "last_run": "",
            "total_articles_seen": 0,
            "websites": {}
        }

        self.save()