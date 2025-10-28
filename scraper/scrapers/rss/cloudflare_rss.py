import requests
from bs4 import BeautifulSoup
from models.raw_events import RawEvent

def scrape_cloudflare_rss():

    URL = "https://blog.cloudflare.com/rss"

    cloudflare_rss_feed = requests.get(URL)

    soup = BeautifulSoup(cloudflare_rss_feed.content, features="xml")

    articles = soup.find_all("item")

    events = []

    company = "CloudFlare"
    source = soup.find("title").text

    for article in articles:
        url = article.find("link").text if article.find("link") else None
        title = article.find("title").text if article.find("title") else None
        date_published = article.find("pubDate").text if article.find("pubDate") else None
        categories = article.find("category").text if article.find("category") else None
        description = article.find("description").text if article.find("description") else None

        raw_event = RawEvent(url, company, source, title, date_published, description)

        events.append(raw_event)

    return events
