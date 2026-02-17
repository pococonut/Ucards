from app.domain.entities.deck import Deck
from app.presentstion.schemas.deck_schemas import DeckResponce


class DeckMapper:
    @staticmethod
    def to_response(deck: Deck) -> DeckResponce:
        """Преобразование доменной сущности в схему ответа"""
        return DeckResponce(
            id=str(deck.id),
            name=deck.name,
            algorithm=deck.algorithm,
        )