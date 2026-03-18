from fastapi import Depends
from sqlalchemy.engine import Connection

from infrastructure.database.core.connection import get_connection
from application.services.card_service import CardService

from application.services.algorithm_service import SM2Service
from infrastructure.database.repositories.card_repository import DBCardRepository
from application.services.deck_service import DeckService
from infrastructure.database.repositories.algorithm_repository import SM2Repository
from infrastructure.database.repositories.deck_repository import DBDeckRepository


def get_repo(conn: Connection = Depends(get_connection)) -> DBCardRepository:
    # Можно вернуть конкретную реализацию
    return DBCardRepository(connection=conn)

def get_user_use_cases(repo: DBCardRepository = Depends(get_repo)) -> CardService:
    return CardService(repo)

# def get_card_service() -> CardService:
#     """
#     Инициализирует объект репозитория и передает его в логику работы методов карточки.
#     """
#     repository = DBCardRepository()
#     return CardService(repository)


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
