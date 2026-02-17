from app.application.services.card_service import CardService
from app.application.services.algorithm_service import SM2Service
from app.infrastructure.repositories.card_repository import DBCardRepository
from app.application.services.deck_service import DeckService
from app.infrastructure.repositories.algorithm_repository import SM2Repository
from app.infrastructure.repositories.deck_repository import DBDeckRepository


def get_card_service() -> CardService:
    """
    Инициализирует объект репозитория и передает его в логику работы методов карточки.
    """
    repository = DBCardRepository()
    return CardService(repository)


def get_deck_service() -> DeckService:
    """
    Инициализирует объект репозитория и передает его в логику работы методов доски.
    """
    repository = DBDeckRepository()
    return DeckService(repository)


def get_sm2_service() -> SM2Service:
    """
    Инициализирует объект репозитория и передает его в логику работы методов алгоритма SM2.
    """
    repository = SM2Repository()
    return SM2Service(repository)
