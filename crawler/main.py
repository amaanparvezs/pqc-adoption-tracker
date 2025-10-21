from db import init_db, insert_event
from scrapers.ibm import scrape_ibm
from scrapers.cloudflare import scrape_cloudflare



def run_all_scrapers():
    print("Initializing DB...")
    init_db()

    print("Running IBM scraper...")
    ibm_events = scrape_ibm()
    print(f"Found {len(ibm_events)} IBM events")

    print("Running Cloudflare scraper...")
    cloudflare_events = scrape_cloudflare()
    print(f"Found {len(cloudflare_events)} Cloudflare events")

    for event in ibm_events:
        insert_event(event)
        print(f"Inserted: {event['url']}")

    for event in cloudflare_events:
        insert_event(event)
        print(f"Inserted: {event['url']}")


if __name__ == "__main__":
    run_all_scrapers()
