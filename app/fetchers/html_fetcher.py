import httpx
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from app.models import Article


def fetch_html(website):
    """
    Fetch articles from a normal HTML webpage.
    """

    response = httpx.get(
        website["url"],
        timeout=30,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    articles = []

    for item in soup.select(website["article_selector"]):

        title_element = item.select_one(website["title_selector"])
        link_element = item.select_one(website["link_selector"])

        if not title_element or not link_element:
            continue

        title = title_element.get_text(strip=True)

        href = (
            link_element.get("href")
            or title_element.get("href")
            or ""
        )

        if not href:
            continue

        url = urljoin(website["url"], href)

        articles.append(
            Article(
                website=website["name"],
                title=title,
                url=url
            )
        )

    return articles