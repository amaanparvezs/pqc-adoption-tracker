import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_ibm():
    base_url = "https://research.ibm.com/blog"
    page = 1

    articles = []
    events = []

    while True:
        url = f"{base_url}?page={page}"
        print(f"scraping IBM Blog page {page}")
        result = requests.get(url, timeout=10)
        if result.status_code != 200:
            print("No more pages or error")
            break
        soup = BeautifulSoup(result.text, "lxml")
        page_articles = soup.select("article")
        articles.extend(page_articles)
        if not articles:
            print("No articles found.")
            break

        page += 1

    # Example selector: Adjust based on IBM blog structure
    for article in articles:
        title_tag = article.find("a")
        date_tag = article.find("time")

        if not title_tag or not date_tag:
            continue

        link = title_tag.get("href")
        if not link.startswith("http"):
            link = "https://research.ibm.com" + link

        # Extract fields
        event = {
            "url": link,
            "company": "IBM",
            "date_published": datetime.fromisoformat(date_tag.get("datetime")) if date_tag.has_attr("datetime") else None,
            "raw_text": title_tag.get_text(strip=True),
            "source": "IBM Research Blog"
        }
        events.append(event)

    print(f"Scrape successful.\nTotal articles scraped: {len(events)}")

    return events
