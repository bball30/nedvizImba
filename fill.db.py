from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from analytics.models import Base, Listing  # Импортируй из своей структуры

# Подключение к базе данных
engine = create_engine("sqlite:///data/listings.db")
Session = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)
session = Session()

# Примеры объявлений
sample_listings = [
    Listing(
        platform="Авито",
        title="2к квартира, 58 м², 6/10 эт.",
        address="Московский проспект, 50",
        district="Московский",
        city="Санкт-Петербург",
        price=8900000,
        price_per_m2=153000,
        area=58,
        rooms=2,
        floor=6,
        total_floors=10,
        house_type="панель",
        realty_type="квартира",
        url="https://example.com/1",
        scam_flag=False,
        published_at=datetime(2024, 5, 10)
    ),
    Listing(
        platform="ЦИАН",
        title="1к студия, 30 м², 3/16 эт.",
        address="Лиговский проспект, 125",
        district="Фрунзенский",
        city="Санкт-Петербург",
        price=5700000,
        price_per_m2=190000,
        area=30,
        rooms=1,
        floor=3,
        total_floors=16,
        house_type="монолит",
        realty_type="студия",
        url="https://example.com/2",
        scam_flag=False,
        published_at=datetime(2024, 5, 12)
    ),
    Listing(
        platform="ДомКлик",
        title="3к квартира, 76 м², 9/12 эт.",
        address="Проспект Науки, 25",
        district="Калининский",
        city="Санкт-Петербург",
        price=10500000,
        price_per_m2=138000,
        area=76,
        rooms=3,
        floor=9,
        total_floors=12,
        house_type="кирпич",
        realty_type="квартира",
        url="https://example.com/3",
        scam_flag=True,
        scam_reason="Подозрительно низкая цена",
        published_at=datetime(2024, 5, 11)
    )
]

# Добавляем и сохраняем
session.add_all(sample_listings)
session.commit()
session.close()
print("База данных успешно заполнена примерами.")
