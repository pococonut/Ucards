from infrastructure.repositories.card_repository import SM2Repository
from domain.entities.card import Card
from domain.interfaces.repositories import CardRepository, IntervalAlgorithm


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

    def calculate_interval(self, I=1, EF=2.5, quality=1):
        EF_new = max(2.5, EF + (0.1 - (4 - quality) * (0.08 + (4 - quality) * 0.02)))
        print(EF + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)))
        I_new = I * EF_new if quality > 2 else 1
        return self._sm2_repository.calculate_interval(I_new, EF_new, quality)


class CardService:
    """
    Содержит бизнес-правила. Не знает, откуда берутся данные, знает только ЧТО с ними делать
    """
    def __init__(self, card_repository: CardRepository):
        self._card_repository = card_repository

    def get_all_cards(self) -> list[Card]:
        return self._card_repository.get_all_cards()
    
    def get_card_by_id(self, card_id: str) -> Card:
        # Здесь может быть бизнес-логика:
        # - валидация card_id
        # - кэширование
        # - преобразование данных
        return self._card_repository.get_card_by_id(card_id)
    
    def add_card(self, card: Card) -> Card:
        new_card = Card(
            id=str(len(self._card_repository.get_all_cards())),
            name=card.name,
            description=card.description,
            interval=1,
            ef=2.5,
            quality=1
        )
        return self._card_repository.add_card(new_card)

    def change_card(self, card_id: str, new_card: Card) -> Card:
        return self._card_repository.change_card(card_id, new_card)
    
    def delete_card(self, card_id: str) -> Card:
        return self._card_repository.delete_card(card_id)
    
    def answer(self, card: Card, quality: int) -> Card:
        sm2_rep = SM2Repository()
        sm2 = SM2Service(sm2_rep)
        new_interval, new_ef = sm2.calculate_interval(card.interval, card.ef, quality)
        card.interval = new_interval
        card.ef = new_ef
        result_card = self.change_card(card.id, card)
        print("res", result_card)
        return result_card
    
