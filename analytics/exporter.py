import pandas as pd
import os

def generate_excel_report(output_path="reports/analytics_report.xlsx"):
    # Примерные данные (заглушка)
    listings = [
        {
            "Платформа": "Авито",
            "Ссылка": "https://example.com/1",
            "Заголовок объявления": "2к квартира, 58 м²",
            "Адрес": "Московский проспект, 50",
            "Район": "Московский",
            "Город": "Санкт-Петербург",
            "Цена": 8900000,
            "Цена за м²": 153000,
            "Площадь (м²)": 58,
            "Кол-во комнат": 2,
            "Этаж": 6,
            "Этажей в доме": 10,
            "Тип дома": "панель",
            "Тип недвижимости": "квартира",
            "Дата публикации": "2024-05-10",
            "Контактное лицо": "Иван",
            "Телефон": "+7 999 123-45-67",
            "Подозрение на скам": False,
            "Причина подозрения": "",
            "Дата анализа": "2025-05-26",
            "Идентификатор объявления": 1001
        }
    ]

    df = pd.DataFrame(listings)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Объявления", index=False)

        # Пустые листы
        pd.DataFrame(columns=["Район", "Средняя цена", "Мин", "Макс"]).to_excel(writer, sheet_name="Статистика по районам", index=False)
        pd.DataFrame(columns=["Дата", "Всего", "Скамов", "Средняя цена"]).to_excel(writer, sheet_name="Сводка", index=False)

    return output_path
