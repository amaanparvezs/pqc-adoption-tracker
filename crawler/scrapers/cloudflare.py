import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_cloudflare():
    base_url = "https://blog.cloudflare.com"
    page = 1

    articles = []
    events = []

    while True:

        url = f"{base_url}/page/{page}"
        print(f"scraping Cloudflare Blog page {page}")
        result = requests.get(url, timeout=10)

        if result.status_code != 200:
            print("No more pages or error")
            break

        soup = BeautifulSoup(result.text, "lxml")
        page_articles = soup.select("a.BlockLink")

        articles.extend(page_articles)
        if not page_articles:
            print("No articles found.")
            break

        articles.extend(page_articles)

        page += 1

    for article in articles:
        title_tag = article
        title_text = title_tag.get_text(strip=True)
        link = title_tag.get("href")

        if not title_text or not link:
            continue

        if link.startswith("/"):
            link = "https://blog.cloudflare.com" + link

        date_tag = article.find_previous("time")
        if date_tag and date_tag.has_attr("datetime"):
            try:
                date_published = datetime.fromisoformat(date_tag.get("datetime").replace("Z", "+00:00"))
            except Exception:
                date_published = None
        else:
            date_published = None

        # Extract fields
        event = {
            "url": link,
            "company": "Cloudflare",
            "date_published": date_published,
            "raw_text": title_text,
            "source": "Cloudflare Blog"
        }
        events.append(event)

    print(f"Cloudflare Scrape complete.\nTotal articles scraped: {len(events)}")

    return events
