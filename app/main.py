from app.config import load_websites
from app.fetchers.rss_fetcher import fetch_rss
from app.fetchers.html_fetcher import fetch_html
from app.logger import log
from app.state import StateManager
from app.telegram import send_message
from app.utils.hashing import generate_hash


def run():

    websites = load_websites()
    state = StateManager()

    new_articles = 0

    for website in websites:

        log.info(f"Checking {website['name']}")

        try:

            if website["type"] == "rss":
                articles = fetch_rss(website["url"])

            elif website["type"] == "html":
                articles = fetch_html(website)

            else:
                log.warning(f"Unsupported website type: {website['type']}")
                continue

            for article in articles:

                article_hash = generate_hash(article.title + article.url)

                if state.has_seen(website["name"], article_hash):
                    continue

                message = (
                    f"🆕 <b>{website['name']}</b>\n\n"
                    f"<b>{article.title}</b>\n\n"
                    f"{article.url}"
                )

                send_message(message)

                state.add_article(
                    website["name"],
                    article_hash
                )

                new_articles += 1

            log.success(
                f"{website['name']} → {len(articles)} articles checked"
            )

        except Exception as e:
            log.error(f"{website['name']} : {e}")

    state.save()

    log.success(f"Finished. {new_articles} new articles found.")