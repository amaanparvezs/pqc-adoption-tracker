import requests
from bs4 import BeautifulSoup
import lxml
from datetime import datetime

def scrape_ibm():
    base_url = "https://research.ibm.com/blog"
    page = 1
    articles = []
    events = []

    while page <= 2:
        url = f"{base_url}?page={page}"
        print(f"Scraping page {page}")
        html_page = requests.get(url, timeout = 10)

        if html_page.status_code != 200:
            print("No more pages or error!")
            break

        soup = BeautifulSoup(html_page.content, "lxml")

        page_articles = soup.find_all("article")

        articles.extend(page_articles)

        page += 1

    for article in articles:

        title_tag = article.find("a")

        article_link = title_tag.get("href")

        if not article_link.startswith("https://"):
            article_link = "https://research.ibm.com" + article_link
        print(article_link)

        article_title = title_tag.get_text(strip=True)

        article_date = article.find("time").get_text(strip=True)
        article_date = datetime.strptime(article_date, "%d %b %Y").date()
        print(article_date)

        event = {
            "url": article_link,
            "title": article_title,
            "date_published": article_date,
            "company": "IBM",
            "source": "IBM Research Blog",
            "raw_text": ""
        }

        events.append(event)

    return events