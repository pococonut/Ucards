from domain.interfaces.repositories import CardRepository


class CardService:
    def __init__(self, card_repository: CardRepository):
        self._card_repository = card_repository

    def get_all_cards(self) -> dict:
        return self._card_repository.get_all_cards()

    