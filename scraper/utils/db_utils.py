from database import session
def save_raw_events_to_db(events: list):
    session = SessionLocal()
    try:
        for event in events:
            db