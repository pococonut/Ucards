from datetime import date

from domain.entities.card import Card
from domain.entities.algorithm import SM2Params
from domain.interfaces.algorithm_repository import IntervalAlgorithmRepository

sm2_params = [
    SM2Params(id="0", interval=1, ef=2.5, quality=1, show_dt=date(year=2025, month=10, day=29)),
    SM2Params(id="1", interval=1, ef=2.5, quality=1, show_dt=date(year=2025, month=10, day=31))
]


class SM2Repository(IntervalAlgorithmRepository):
    """
    Реализация взаимодействия с базой данных для алгоритма SM2.
    """

    def calculate_interval(self, card_id: str, quality: int) -> SM2Params:
        pass

    def get_card_params(self, card_id: str) -> SM2Params:
        """
        Возвращает параметры выбранного алгоритма для карточки.

        Args:
            card_id (str): Уникальный идентификатор карточки.

        Returns:
            SM2Params: Параметры алгоритма.
        """
        card_params = list(filter(lambda params: params.id == card_id, sm2_params))
        if not card_params:
            params = SM2Params(id=card_id, interval=1, ef=2.5, quality=1, show_dt=date.today())
            card_params = self.add_card_params(card_id, params=params)
        result: SM2Params = card_params[0]
        return result
    
    def add_card_params(self, card_id: str, params: SM2Params) -> SM2Params:
        """
        Сохраняет параметры выбранного алгоритма для карточки.

        Args:
            card_id (str): Уникальный идентификатор карточки.
            params: параметры алгоритма.

        Returns:
            SM2Params: Параметры алгоритма для карточки.
        """
        card_params = list(filter(lambda params: params.id == card_id, sm2_params))
        if card_params:
            card = card_params[0]
            card.ef = params.ef
            card.interval = params.interval
            card.quality = params.quality
            card.show_dt = params.show_dt
        else:
            sm2_params.append(params)

        result = list(filter(lambda params: params.id == card_id, sm2_params))
        return result

    def get_learning_cards(self, cards: list[Card]) -> list[Card]:
        pass