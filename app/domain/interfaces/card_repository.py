from abc import ABC

from domain.entities.card import Card


class CardRepository(ABC):
    """
    Контракт, который говорит "любой репозиторий карточек ДОЛЖЕН уметь возвращать все карточки"
    """
    @classmethod
    def get_all_cards(self) -> list[Card]:
        """Получить все карты"""
        pass

    @classmethod
    def get_card_by_id(self) -> Card:
        """Получить карту по ID"""
        pass
    
    @classmethod
    def add_card(self, Card) -> Card:
        """Добавить карточку"""
        pass

    @classmethod
    def change_card(self, card_id, new_card) -> Card:
        """Изменить карточку"""
        pass
    
    @classmethod
    def delete_card(self, card_id) -> Card:
        """Удалить карточку"""
        pass

    @classmethod
    def answer(self, card: Card, quality) -> Card:
        """Ответить на карточку"""
        pass