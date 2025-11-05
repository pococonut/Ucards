from domain.entities.card import Card
from domain.entities.deck import Deck
from domain.interfaces.deck_repository import DeckRepository


class DeckService:
    """
    Содержит бизнес-правила. Не знает, откуда берутся данные, знает только ЧТО с ними делать
    """
    def __init__(self, deck_repository: DeckRepository):
        self._deck_repository = deck_repository

    def get_all_decks(self) -> list[Deck]:
        return self._deck_repository.get_all_decks()
    
    def get_deck_by_id(self, deck_id: str) -> Deck:
        return self._deck_repository.get_deck_by_id(deck_id)
    
    def get_cards(self, deck_id) -> list[Card]:
        return self._deck_repository.get_cards(deck_id)
    
    def add_deck(self, new_deck: Deck) -> Deck:
        return self._deck_repository.add_deck(new_deck)

    def change_deck(self, deck_id: str, new_deck: Deck) -> Deck:
        return self._deck_repository.change_deck(deck_id, new_deck)
    
    def delete_deck(self, deck_id: str) -> Deck:
        return self._deck_repository.delete_deck(deck_id)
    
    
