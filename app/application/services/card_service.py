from domain.entities.card import Card
from domain.interfaces.repositories import CardRepository


class CardService:
    """
    Содержит бизнес-правила. Не знает, откуда берутся данные, знает только ЧТО с ними делать
    """
    def __init__(self, card_repository: CardRepository):
        self._card_repository = card_repository

    def get_all_cards(self) -> list[Card]:
        return self._card_repository.get_all_cards()
    
    def get_card_by_id(self, card_id) -> Card:
        # Здесь может быть бизнес-логика:
        # - валидация card_id
        # - кэширование
        # - преобразование данных
        return self._card_repository.get_card_by_id(card_id)
    
    def add_card(self, card: Card) -> Card:
        delay = {
            "Easy": 7,
            "Good": 3,
            "Hard": 1,
            "Bad": 0
                }
        
        new_card = Card(
            id=str(len(self._card_repository.get_all_cards())),
            name=card.name,
            description=card.description,
            next_review=card.next_review + delay.get(card.level, 0),
            level=card.level
        )
        return self._card_repository.add_card(new_card)


    def change_card(self, card_id, new_card: Card) -> Card:
        return self._card_repository.change_card(card_id, new_card)
    
    def delete_card(self, card_id: str) -> Card:
        return self._card_repository.delete_card(card_id)
    