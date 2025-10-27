from abc import ABC


class IntervalAlgorithmRepository(ABC):
    "Контракт алгоритма для повторения"
    @classmethod
    def calculate_interval(self, card_id: str, quality: int) -> dict:
        "Вычисление интервала для повтора карточки"
        pass

    @classmethod
    def get_card_params(self, card_id: str) -> dict:
        pass

    @classmethod
    def add_card_params(self, card_id: str, params: dict) -> dict:
        pass