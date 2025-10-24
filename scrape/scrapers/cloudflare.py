import requests
from bs4 import BeautifulSoup
import time, random
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def create_session():
    """Create a session with retries and realistic headers."""
    session = requests.Session()

    retries = Retry(
        total=5,
        backoff_factor=1.5,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))

    # Randomly rotate User-Agent
    HEADERS = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/117.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/118.0 Safari/537.36"
        ]),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    session.headers.update(HEADERS)
    return session


def fetch_page(session, url):
    """Fetch a single page with retry-safe logic."""
    try:
        r = session.get(url, timeout=(5, 30))
        r.raise_for_status()
        return r.text
    except requests.exceptions.ReadTimeout:
        print(f"⚠️ Timeout on {url}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching {url}: {e}")
        return None


def polite_wait(page):
    """Wait in a human-like manner."""
    if page % 10 == 0:
        print("😴 Taking a longer break to avoid throttling...")
        time.sleep(random.uniform(10, 20))
    else:
        time.sleep(random.uniform(2, 5))


def scrape_cloudflare():
    """Scrape all Cloudflare blog posts across paginated pages."""
    base_url = "https://blog.cloudflare.com"
    total_pages = 167  # known from manual inspection
    session = create_session()

    page = 1

    while page <= total_pages:
        url = f"{base_url}/page/{page}/"
        print(f"🕷️  Scraping Cloudflare Blog page {page}")

        html = fetch_page(session, url)
        if not html:
            print(f"⚠️ Skipping page {page} due to error.")
            polite_wait(page)
            continue

        polite_wait(page)
        page += 1
    return page


def main():
    page = scrape_cloudflare()
    print(page)


if __name__ == "__main__":
    main()
