from domain.entities.deck import Deck
from domain.interfaces.deck_repository import DeckRepository


decks = [
    Deck(id="0", name="Langs", algorithm="sm2")
]


class DBDeckRepository(DeckRepository):
    """
    Конкретная реализация, которая знает, КАК именно получать данные (из БД, файла, API и т.д.)
    """
    def get_all_decks(self) -> list[Deck]:
        return decks
    
    def get_deck_by_id(self, deck_id: str) -> Deck | None:
        for deck in decks:
            if deck.id == deck_id:
                return deck
        return None
    
    def add_deck(self, deck: Deck) -> Deck:
        decks.append(deck)
        return deck
    
    def change_deck(self, deck_id: str, new_deck: Deck) -> Deck:
        deck = next(filter(lambda deck: deck.id == deck_id, decks))
        deck.name = new_deck.name
        deck.algorithm = new_deck.algorithm
        return deck   

    def delete_deck(self, deck_id: str) -> Deck:
        deck = next(filter(lambda deck: deck.id == deck_id, decks))
        deck_index = decks.index(deck)
        return decks.pop(deck_index)
    
