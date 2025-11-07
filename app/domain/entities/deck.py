from dataclasses import dataclass


@dataclass
class Deck:
    """
    Класс для представления доски.

    Attributes:
        id: Уникальный идентификатор.
        name: Название доски.
        algorithm: Алгоритм повторения карточек.
    """
    id: str
    name: str
    algorithm: str
