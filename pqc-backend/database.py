from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://pqc_user:pqcadoptiontracker@localhost:5432/pqc_tracker"
engine = create_engine(db_url)
session = sessionmaker(autocomit=False, autoflush=False, bind=engine)