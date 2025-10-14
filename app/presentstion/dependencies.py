from application.services.card_service import CardService
from infrastructure.repositories.card_repository import DBCardRepository


def get_card_service():
    repository = DBCardRepository()
    return CardService(repository)


