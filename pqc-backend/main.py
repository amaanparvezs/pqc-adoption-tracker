from typing import Union

from fastapi import FastAPI

from database import session

app = FastAPI()

@app.get("/")
def get_raw_events():
    db = session()
    db.query()