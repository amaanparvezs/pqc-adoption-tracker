import psycopg2
from psycopg2.extras import DictCursor

def get_connection():
    return psycopg2.connect(
        dbname="pqc_tracker",
        user="pqc_user",
        password="pqcadoptiontracker",
        host="localhost",
        port="5432"
    )

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS raw_events (
        id SERIAL PRIMARY KEY,
        url TEXT UNIQUE,
        company TEXT,
        date_published TIMESTAMP,
        raw_text TEXT,
        source TEXT
    )
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_event(event):
    """Insert a single event (dict) into DB"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO raw_events (url, company, date_published, raw_text, source)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (url) DO NOTHING
    """, (
        event["url"],
        event["company"],
        event["date_published"],
        event["raw_text"],
        event["source"]
    ))
    conn.commit()
    cur.close()
    conn.close()
