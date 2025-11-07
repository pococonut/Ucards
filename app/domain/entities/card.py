from dataclasses import dataclass


@dataclass
class Card:
    """
    Класс для представления карточки.

    Attributes:
        id: Уникальный идентификатор.
        deck_id: Уникальный идентификатор доски.
        name: Лицевая сторона карточки.
        description: Задняя сторона карточки.
    """
    id: str
    deck_id: str
    name: str
    description: str
