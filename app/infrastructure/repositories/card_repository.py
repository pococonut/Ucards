from domain.entities.card import Card
from domain.interfaces.repositories import CardRepository, IntervalAlgorithmRepository


cards = [
    Card(id="0", name="hello", description="привет", interval=1, ef=2.5, quality=1),
    Card(id="1", name="world", description="мир", interval=1, ef=2.5, quality=1)
]


class SM2Repository(IntervalAlgorithmRepository):
    """
    Реализация алгоритма SM-2
    """
    def calculate_interval(self, card: Card, q: int):
        return card


class DBCardRepository(CardRepository):
    """
    Конкретная реализация, которая знает, КАК именно получать данные (из БД, файла, API и т.д.)
    """
    def get_all_cards(self) -> list[Card]:
        return cards
    
    def get_card_by_id(self, card_id: str) -> Card | None:
        for card in cards:
            if card.id == card_id:
                return card
        return None
    
    def add_card(self, card: Card) -> Card:
        cards.append(card)
        return card
    
    def change_card(self, card_id: str, new_card: Card) -> Card:
        card = next(filter(lambda card: card.id == card_id, cards))
        card.name = new_card.name
        card.description = new_card.description
        card.interval = new_card.interval
        card.ef = new_card.ef
        card.quality = new_card.quality
        return card   

    def delete_card(self, card_id: str) -> Card:
        card = next(filter(lambda card: card.id == card_id, cards))
        card_index = cards.index(card)
        return cards.pop(card_index)
    
