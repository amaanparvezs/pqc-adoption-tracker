import uuid
from datetime import date

class RawEvent:
    id: uuid
    url: str
    company: str
    source: str
    title: str
    date_published: date
    description: str

    def __init__(self, url, company, source, title, date_published, description):
        self.url = url
        self.company = company
        self.source = source
        self.title = title
        self.date_published = date_published
        self.description = description