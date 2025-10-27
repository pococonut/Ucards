from domain.entities.algorithm import SM2Params
from infrastructure.repositories.algorithm_repository import SM2Repository


class SM2Service:
    """
    Реализация алгоритма SM-2
    I — Интервал до следующего повторения (в днях).
    EF — Фактор Легкости (E-Factor). Определяет, насколько быстро растет интервал. Начинается с 2.5.
    q — Качество ответа от 1 до 4, где:
        4 — Идеальный ответ
        3 — Правильный ответ
        2 — Правильный ответ с затруднением
        1 — Неправильный ответ
    """
    def __init__(self, sm2_repository: SM2Repository):
        self._sm2_repository = sm2_repository

    def calculate_interval(self, card_id: str, quality: int):
        card_params = self._sm2_repository.get_card_params(card_id)
        EF = card_params.interval
        I  = card_params.ef

        EF_new = max(2.5, EF + (0.1 - (4 - quality) * (0.08 + (4 - quality) * 0.02)))
        I_new = I * EF_new if quality > 2 else 1

        params = SM2Params(id=card_id, ef=EF_new, interval=I_new, quality=quality)
        
        self._sm2_repository.add_card_params(card_id, params)
        return self._sm2_repository.calculate_interval(card_id, quality)

    def get_card_params(self, card_id: str) -> SM2Params:
        return self._sm2_repository.get_card_params(card_id)
    
    def add_card_params(self, card_id: str, params: SM2Params) -> SM2Params:
        return self._sm2_repository.add_card_params(card_id, params)
