from pydantic import BaseModel


class DeckBase(BaseModel):
    """
    Модель для параметров доски.

    Attributes:
        name: Название доски.
        algorithm: Выбранный алгоритм повторения карточек. 
    """
    name: str
    algorithm: str


class DeckResponce(DeckBase):
    """
    Схема для ответа с Deck.

    Attributes:
        id: Уникальный идентификатор доски.
    """
    id: str