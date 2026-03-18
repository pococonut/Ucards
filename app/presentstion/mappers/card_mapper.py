
from domain.entities.card import Card
from presentstion.schemas.card_schemas import CardResponse


class CardMapper:
    @staticmethod
    def to_response(card: Card) -> CardResponse:
        """Преобразование доменной сущности в схему ответа"""
        return CardResponse(
            id=card.id,
            name=card.name,
            description=card.description,
            deck_id=card.deck_id
        )