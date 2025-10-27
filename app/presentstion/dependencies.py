from application.services.card_service import CardService
from application.services.algorithm_service import SM2Service
from infrastructure.repositories.card_repository import DBCardRepository
from application.services.deck_service import DeckService
from infrastructure.repositories.algorithm_repository import SM2Repository
from infrastructure.repositories.deck_repository import DBDeckRepository


def get_card_service():
    """
    Собирает все части воедино — "склеивающий" слой
    """
    repository = DBCardRepository()
    return CardService(repository)


def get_deck_service():
    repository = DBDeckRepository()
    return DeckService(repository)


def get_sm2_service():
    repository = SM2Repository()
    return SM2Service(repository)
