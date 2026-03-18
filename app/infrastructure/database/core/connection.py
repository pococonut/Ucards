import os

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Настройка движка (параметры из конфигурации)
engine = create_engine(DB_URL, echo=True)


def get_connection():
    """Функция для получения соединения (можно использовать как зависимость)."""
    with engine.begin() as conn:
        yield conn
