import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_ibm():
    url = "https://research.ibm.com/blog"   # IBM Research Blog
    res = requests.get(url, timeout=10)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    events = []

    # Example selector: Adjust based on IBM blog structure
    articles = soup.select("article")  # Each article block
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

    return events
