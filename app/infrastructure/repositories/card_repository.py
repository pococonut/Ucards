from domain.entities.sm2_params import SM2Params
from domain.entities.card import Card
from domain.interfaces.repositories import CardRepository, IntervalAlgorithmRepository


cards = [
    Card(id="0", name="hello", description="привет"),
    Card(id="1", name="world", description="мир")
]

sm2_params = [
    SM2Params(id="0", interval=1, ef=2.5, quality=1),
    SM2Params(id="1", interval=1, ef=2.5, quality=1)
]


class SM2Repository(IntervalAlgorithmRepository):
    """
    Реализация алгоритма SM-2
    """
    def calculate_interval(self, card_id: str, q: int) -> SM2Params:
        return next(filter(lambda params: params.id == card_id, sm2_params))
    
    def get_card_params(self, card_id: str) -> SM2Params:
        return next(filter(lambda params: params.id == card_id, sm2_params))
    
    def add_card_params(self, card_id: str, params: SM2Params) -> SM2Params:
        card_params = list(filter(lambda params: params.id == card_id, sm2_params))
        if card_params:
            card = card_params[0]
            card.ef = params.ef
            card.interval = params.interval
            card.quality = params.quality
        else:
            sm2_params.append(params)
        return next(filter(lambda params: params.id == card_id, sm2_params))


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
        return card   

    def delete_card(self, card_id: str) -> Card:
        card = next(filter(lambda card: card.id == card_id, cards))
        card_index = cards.index(card)
        return cards.pop(card_index)
    
