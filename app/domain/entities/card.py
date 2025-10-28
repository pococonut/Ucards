from dataclasses import dataclass


@dataclass
class Card:
    """
    Бизнес-сущность 'Карточка'.
    Содержит чистые данные и бизнес-правила. 
    Не знает о БД, API и других внешних вещах.
    """
    id: str
    deck_id: str
    name: str
    description: str
