from datetime import date

from domain.entities.algorithm import SM2Params
from domain.interfaces.algorithm_repository import IntervalAlgorithmRepository

sm2_params = [
    SM2Params(id="0", interval=1, ef=2.5, quality=1, show_dt=date(year=2025, month=10, day=29)),
    SM2Params(id="1", interval=1, ef=2.5, quality=1, show_dt=date(year=2025, month=10, day=31))
]


class SM2Repository(IntervalAlgorithmRepository):
    """
    Реализация алгоритма SM-2
    """

    def get_card_params(self, card_id: str) -> SM2Params:
        card_params = list(filter(lambda params: params.id == card_id, sm2_params))
        if not card_params:
            params = SM2Params(id=card_id, interval=1, ef=2.5, quality=1, show_dt=date.today())
            card_params = self.add_card_params(card_id, params=params)
        return card_params[0]
    
    def add_card_params(self, card_id: str, params: SM2Params) -> SM2Params:
        card_params = list(filter(lambda params: params.id == card_id, sm2_params))
        if card_params:
            card = card_params[0]
            card.ef = params.ef
            card.interval = params.interval
            card.quality = params.quality
            card.show_dt = params.show_dt
        else:
            sm2_params.append(params)
        return list(filter(lambda params: params.id == card_id, sm2_params))
