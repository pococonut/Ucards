from datetime import date
from app.domain.entities.card import Card
from app.domain.entities.algorithm import SM2Params
from app.infrastructure.repositories.algorithm_repository import SM2Repository


class SM2Service:
    """
    Реализация логики работы алгоритма SM2.
    """
    
    def __init__(self, sm2_repository: SM2Repository):
        self._sm2_repository = sm2_repository

    def calculate_interval(self, card_id: str, quality: int) -> SM2Params:
        """
        Вычисляет интервал для повтора карточки.

        Реализация алгоритма SM-2
        I — Интервал до следующего повторения (в днях).
        EF — Фактор Легкости (E-Factor). Определяет, насколько быстро растет интервал. Начинается с 2.5.
        q — Качество ответа от 1 до 4, где:
        4 — Идеальный ответ
        3 — Правильный ответ
        2 — Правильный ответ с затруднением
        1 — Неправильный ответ

        Args:
            card_id (str): Уникальный идентификатор карточки.
            quality (int): Качество ответа.

        Returns:
            SM2Params: Обновленные параметры алгоритма для карточки.
        """
        card_params = self._sm2_repository.get_card_params(card_id)
        EF = card_params.interval
        I  = card_params.ef
        show_dt = card_params.show_dt.toordinal()

        EF_new = max(1.3, EF + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)))
        I_new = round(I * EF_new) if quality > 2 else 1
        
        if quality > 2:
            show_dt_new = date.fromordinal(show_dt + I_new) 
            if show_dt_new < date.today():
                show_dt_new = date.fromordinal(date.today().toordinal() + I_new)
        else:
            show_dt_new = date.fromordinal(date.today().toordinal() + 1)
            
        params = SM2Params(id=card_id, ef=EF_new, interval=I_new, quality=quality, show_dt=show_dt_new)
        
        self.add_card_params(card_id, params)
        return params

    def get_card_params(self, card_id: str) -> SM2Params:
        """
        Возвращает параметры выбранного алгоритма для карточки.

        Args:
            card_id (str): Уникальный идентификатор карточки.

        Returns:
            SM2Params: Параметры алгоритма.
        """
        return self._sm2_repository.get_card_params(card_id)
    
    def get_learning_cards(self, cards: list[Card]) -> list[str]:
        """
        Возвращает карточки для повторения согласно интервалу рассчитанного алгоритмом.

        Args:
            cards (list): Список карточек доски.
            
        Returns:
            list[str]: ИСписок идентификаторов карточек для изучения.
        """
        res = []
        for card in cards:
            params: SM2Params = self.get_card_params(card.id)
            if params.show_dt <= date.today():
                res.append(card.id)
        return res

    def add_card_params(self, card_id: str, params: SM2Params) -> SM2Params:
        """
        Сохраняет параметры выбранного алгоритма для карточки.

        Args:
            card_id (str): Уникальный идентификатор карточки.
            params: параметры алгоритма.

        Returns:
            SM2Params: Параметры алгоритма для карточки.
        """
        return self._sm2_repository.add_card_params(card_id, params)
