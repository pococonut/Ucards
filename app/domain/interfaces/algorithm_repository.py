from abc import ABC, abstractmethod

from domain.entities.algorithm import SM2Params
from domain.entities.card import Card


class IntervalAlgorithmRepository(ABC):
    """
    Интерфейс метода алгоритма повторения карточек
    """
    @abstractmethod
    def calculate_interval(self, card_id: str, quality: int) -> SM2Params:
        """
        Вычисляет интервал для повтора карточки.

        Args:
            card_id (str): Уникальный идентификатор карточки.
            quality (int): Качество ответа.

        Returns:
            Интервал повторения карточки.
        """
        pass

    @abstractmethod
    def get_card_params(self, card_id: str) -> SM2Params:
        """
        Возвращает параметры выбранного алгоритма для карточки.

        Args:
            card_id (str): Уникальный идентификатор карточки.

        Returns:
            Параметры алгоритма.
        """
        pass

    @abstractmethod
    def add_card_params(self, card_id: str, params: SM2Params) -> SM2Params:
        """
        Сохраняет параметры выбранного алгоритма для карточки.

        Args:
            card_id (str): Уникальный идентификатор карточки.
            params: параметры алгоритма.

        Returns:
            Параметры алгоритма для карточки.
        """
        pass

    @abstractmethod
    def get_learning_cards(self, cards: list[Card]) -> list[Card]:
        """
        Возвращает карточки для повторения согласно интервалу рассчитанного алгоритмом.

        Args:
            cards (list[Card]): Список карточек доски.
            
        Returns:
            Карточки для повторения.
        """
        pass