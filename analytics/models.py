from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    platform = Column(String)
    title = Column(String)
    address = Column(String)
    district = Column(String)
    city = Column(String)
    price = Column(Float)
    price_per_m2 = Column(Float)
    area = Column(Float)
    rooms = Column(Integer)
    floor = Column(Integer)
    total_floors = Column(Integer)
    house_type = Column(String)
    realty_type = Column(String)
    url = Column(String)
    scam_flag = Column(Boolean, default=False)
    scam_reason = Column(String, nullable=True)
    published_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
