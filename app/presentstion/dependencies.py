from application.services.card_service import CardService, SM2Service
from infrastructure.repositories.card_repository import DBCardRepository, SM2Repository


def get_card_service():
    """
    Собирает все части воедино — "склеивающий" слой
    """
    repository = DBCardRepository()
    return CardService(repository)


def get_sm2_service():
    repository = SM2Repository()
    return SM2Service(repository)
