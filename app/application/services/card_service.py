from infrastructure.repositories.card_repository import SM2Repository
from domain.entities.card import Card
from domain.interfaces.repositories import CardRepository


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

    def calculate_interval(self, card: Card, quality: int):
        EF = card.interval
        I  = card.ef

        EF_new = max(2.5, EF + (0.1 - (4 - quality) * (0.08 + (4 - quality) * 0.02)))
        I_new = I * EF_new if quality > 2 else 1

        card.ef = EF_new
        card.interval = I_new
        card.quality = quality

        return self._sm2_repository.calculate_interval(card, quality)


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
    
    
