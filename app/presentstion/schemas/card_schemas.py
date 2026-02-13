from pydantic import BaseModel
from typing import Any


class CardBase(BaseModel):
    """
    Схема параметров карточки.

    Attributes:
        name: Лицевая сторона карточки.
        description: Задняя сторона карточки.
        deck_id: Идентификатор доски к которой принадлежит карточка.
    """
    name: str
    description: str
    deck_id: str


class CardResponse(CardBase):
    """
    Схема для ответа с Card.

    Attributes:
        id: Уникальный идентификатор карточки.
    """
    id: str


# class UpdatedParameter(BaseModel):
#     parameter: str
#     value: Any
