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
    Реализация алгоритма SM-2
    """
    def calculate_interval(self, card_id: str, q: int) -> SM2Params:
        return next(filter(lambda params: params.id == card_id, sm2_params))
    
    def get_card_params(self, card_id: str) -> SM2Params:
        return next(filter(lambda params: params.id == card_id, sm2_params))
    
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
        return next(filter(lambda params: params.id == card_id, sm2_params))
