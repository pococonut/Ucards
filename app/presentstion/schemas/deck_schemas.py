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


class DeckSh(DeckBase):
    """
    Модель параметров доски с идентификатором.

    Attributes:
        id: Уникальный идентификатор доски.
    """
    id: str