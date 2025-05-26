from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from analytics.models import Base

engine = create_engine("sqlite:///data/listings.db", echo=True)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
