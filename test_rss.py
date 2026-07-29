from app.fetchers.rss_fetcher import fetch_rss

RSS_URL = "https://feeds.feedburner.com/TheHackersNews"

articles = fetch_rss(RSS_URL)

print(f"Found {len(articles)} articles\n")

for article in articles[:5]:
    print("Title :", article.title)
    print("URL   :", article.url)
    print("Date  :", article.published)
    print("-" * 80)
    