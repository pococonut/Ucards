from domain.interfaces.repositories import CardRepository


cards = [
    {"id": "0", "name": "hello", "description": "привет"}, 
    {"id": "1", "name": "world", "description": "мир"}
]


class DBCardRepository(CardRepository):
    def get_all_cards(self) -> list[dict]:
        return cards
    
