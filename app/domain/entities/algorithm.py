from dataclasses import dataclass
from datetime import date


@dataclass
class SM2Params:
    """
    Класс для представления алгоритма SM2.

    Attributes:
        id: Уникальный иденттификатор.
        interval: Количество дней через которое показать карточку.
        ef: Коэффициент эффективности.
        quality: Качество ответа (от 0 до 4).
        show_dt: Дата в которую показать карточку.
    """
    id: str
    interval: float
    ef: float
    quality: int
    show_dt: date