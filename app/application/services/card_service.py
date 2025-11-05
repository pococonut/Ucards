from domain.entities.card import Card
from domain.interfaces.card_repository import CardRepository


class CardService:
    """
    Содержит бизнес-правила. Не знает, откуда берутся данные, знает только ЧТО с ними делать
    """
    def __init__(self, card_repository: CardRepository):
        self._card_repository = card_repository

    def get_all_cards(self) -> list[Card]:
        return self._card_repository.get_all_cards()
    
    def get_card_by_id(self, card_id: str) -> Card:
        return self._card_repository.get_card_by_id(card_id)
    
    def add_card(self, new_card: Card) -> Card:
        return self._card_repository.add_card(new_card)

    def change_card(self, card_id: str, new_card: Card) -> Card:
        return self._card_repository.change_card(card_id, new_card)
    
    def delete_card(self, card_id: str) -> Card:
        return self._card_repository.delete_card(card_id)
    
    
