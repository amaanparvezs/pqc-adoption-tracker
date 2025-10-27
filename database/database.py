from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DB_URL = "postgresql://pqc_user:pqcadoptiontracker@localhost:5432/pqc_tracker"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)