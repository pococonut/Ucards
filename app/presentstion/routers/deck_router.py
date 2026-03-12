from fastapi import APIRouter, Depends, HTTPException

from domain.entities.deck import Deck
from domain.entities.card import Card
from presentstion.mappers.card_mapper import CardMapper
from presentstion.mappers.deck_mapper import DeckMapper
from presentstion.schemas.card_schemas import CardResponse
from application.services.algorithm_service import SM2Service
from presentstion.dependencies import get_deck_service, get_sm2_service
from application.services.deck_service import DeckService
from application.services.deck_service import DeckService
from presentstion.schemas.deck_schemas import DeckBase, DeckResponce


router = APIRouter()


@router.get("/deck", tags=['deck'])
async def get_decks(deck_service: DeckService = Depends(get_deck_service)) -> list[DeckResponce]:
    """
    Возвращает все доски.

    Returns:
        list[DeckResponce]: Все доски.
    """
    result: list[DeckResponce] = [DeckMapper.to_response(deck) for deck in deck_service.get_all_decks()]
    return result


@router.get("/deck/{deck_id}", tags=['deck'])
async def get_deck(deck_id: str, 
                   deck_service: DeckService = Depends(get_deck_service)) -> DeckResponce:
    """
    Возвращает доску по id.

    Args:
        deck_id (str): Уникальный идентификатор доски.

    Returns:
        DeckResponce: Доска.
    """
    deck: Deck = deck_service.get_deck_by_id(deck_id)
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found")
    
    responce: DeckResponce = DeckMapper.to_response(deck)
    return deck


@router.get("/deck/{deck_id}/cards", tags=['deck'])
async def get_cards(deck_id: str,
              deck_service: DeckService = Depends(get_deck_service)) -> list[CardResponse]:
    """
    Возвращает карточки для доски.

    Args:
        deck_id (str): Уникальный идентификатор доски.

    Returns:
        list[CardResponse]: Список карт доски.
    """
    result: list[CardResponse] = [CardMapper.to_response(card) for card in deck_service.get_cards(deck_id)]
    return result


@router.get("/deck/{deck_id}/learn", tags=['deck'])
async def learn_cards(deck_id: str,
              deck_service: DeckService = Depends(get_deck_service),
              algorithm_service: SM2Service = Depends(get_sm2_service)) -> list[str]:
    """
    Возвращает карточки для изучения.

    Args:
        deck_id (str): Уникальный идентификатор доски.

    Returns:
        list[str]: Список идентификаторов карточек для изучения.
    """
    cards = deck_service.get_cards(deck_id)
    learning_cards: list[str] = algorithm_service.get_learning_cards(cards)
    return learning_cards


@router.post("/deck", tags=['deck'])
async def post_deck(deck: DeckBase, 
                    deck_service: DeckService = Depends(get_deck_service)) -> DeckResponce:
    """
    Добавляет новую доску.

    Args:
        deck (DeckBase): Тело новой доски.

    Returns:
        DeckResponce: Добавленная доска.
    """
    result: DeckResponce = DeckMapper.to_response(deck_service.add_deck(deck))
    return result


@router.put("/deck/{deck_id}", tags=['deck'])
async def put_deck(new_deck: DeckBase, 
             deck_id: str,
             deck_service: DeckService = Depends(get_deck_service)) -> DeckResponce:
    """
    Заменяет параметры доски.

    Args:
        deck_id (str): Уникальный идентификатор доски, которую необходимо изменить.
        new_deck (DeckBase): Тело доски с обновленными параметрами.
    
    Returns:
        DeckResponce: Обновленная доска.
    """
    result: DeckResponce = DeckMapper.to_response(deck_service.change_deck(deck_id, new_deck))
    return result


@router.delete("/deck/{deck_id}", tags=['deck'])
async def del_deck(deck_id: str,
             deck_service: DeckService = Depends(get_deck_service)) -> DeckResponce:
    """
    Удаляет доску.
    
    Args:
        deck_id (str): Уникальный идентификатор доски, которую необходимо удалить.
    
    Returns:
        DeckResponce: Удаленная доска.
    """
    result: DeckResponce = DeckMapper.to_response(deck_service.delete_deck(deck_id))
    return result


