from abc import ABC

from domain.entities.card import Card
from domain.entities.deck import Deck


class DeckRepository(ABC):
    @classmethod
    def get_all_decks(self) -> list[Deck]:
        """Получить все доски"""
        pass

    @classmethod
    def get_deck_by_id(self) -> Deck:
        """Получить доску по ID"""
        pass

    @classmethod
    def get_cards(self, deck_id: str) -> list[Card]:
        """Получить карточки"""
        pass
    
    @classmethod
    def add_deck(self, new_deck: Deck) -> Deck:
        """Добавить доску"""
        pass

    @classmethod
    def change_deck(self, deck_id, new_deck: Deck) -> Deck:
        """Изменить доску"""
        pass
    
    @classmethod
    def delete_deck(self, deck_id: str) -> Deck:
        """Удалить доску"""
        pass
