import cloudscraper
from tenacity import retry, stop_after_attempt, wait_fixed

scraper = cloudscraper.create_scraper()


@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(5)
)
def get(url):

    response = scraper.get(
        url,
        timeout=30,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    response.raise_for_status()

    return response