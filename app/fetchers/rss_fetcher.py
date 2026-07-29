import feedparser
from app.models import Article


def fetch_rss(url: str):
    feed = feedparser.parse(url)
    articles = []

    for entry in feed.entries:
        articles.append(
            Article(
                website=url,
                title=entry.get("title", "").strip(),
                url=entry.get("link", "").strip(),
                summary=entry.get("summary", "").strip(),
                published=entry.get("published", ""),
                author=entry.get("author", ""),
            )
        )

    return articles