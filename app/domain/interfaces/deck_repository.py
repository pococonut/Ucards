from abc import ABC

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
    def add_deck(self, Deck) -> Deck:
        """Добавить доску"""
        pass

    @classmethod
    def change_deck(self, deck_id, new_deck) -> Deck:
        """Изменить доску"""
        pass
    
    @classmethod
    def delete_deck(self, deck_id) -> Deck:
        """Удалить доску"""
        pass
