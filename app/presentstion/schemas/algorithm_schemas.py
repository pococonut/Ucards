from datetime import date

from pydantic import BaseModel


class SM2Base(BaseModel):
    """
    Схема алгоритма SM2.

    Attributes:
        interval: Количество дней через которое показать карточку.
        ef: Коэффициент эффективности.
        quality: Качество ответа (от 0 до 4).
        show_dt: Дата в которую показать карточку.
    """
    interval: float
    ef: float
    quality: int
    show_dt: date


class SM2Response(SM2Base):
    """
    Схема для ответа с SM2.

    Attributes:
        id: Уникальный иденттификатор.
    """
    id: str