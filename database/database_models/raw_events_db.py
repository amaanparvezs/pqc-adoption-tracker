from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, UUID, String, Float, Text, Date
import uuid

from .base import Base

class RawEventsDb(Base):

    __tablename__ = "raw_events"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    url = Column(String, index=True)
    company = Column(String)
    source = Column(String)
    title = Column(String)
    date_published = Column(Date)
    description = Column(Text)
