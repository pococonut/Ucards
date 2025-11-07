from application.services.card_service import CardService
from application.services.algorithm_service import SM2Service
from infrastructure.repositories.card_repository import DBCardRepository
from application.services.deck_service import DeckService
from infrastructure.repositories.algorithm_repository import SM2Repository
from infrastructure.repositories.deck_repository import DBDeckRepository


def get_card_service():
    """
    Инициализирует объект репозитория и передает его в логику работы методов карточки.
    """
    repository = DBCardRepository()
    return CardService(repository)


def get_deck_service():
    """
    Инициализирует объект репозитория и передает его в логику работы методов доски.
    """
    repository = DBDeckRepository()
    return DeckService(repository)


def get_sm2_service():
    """
    Инициализирует объект репозитория и передает его в логику работы методов алгоритма SM2.
    """
    repository = SM2Repository()
    return SM2Service(repository)
