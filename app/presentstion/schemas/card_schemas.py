from pydantic import BaseModel
from typing import Any


class CardBase(BaseModel):
    """
    Модель для параметров карточки.

    Attributes:
        name: Лицевая сторона карточки.
        description: Задняя сторона карточки.
        deck_id: Идентификватор доски к которой принадлежит карточка. 
    """
    name: str
    description: str
    deck_id: str


class CardSh(CardBase):
    """
    Модель параметров карточки с идентификатором.

    Attributes:
        id: Уникальный идентификатор карточки.
    """
    id: str


# class UpdatedParameter(BaseModel):
#     parameter: str
#     value: Any
