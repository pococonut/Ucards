from fastapi import APIRouter, Depends, HTTPException

from presentstion.dependencies import get_card_service, get_sm2_service
from application.services.card_service import CardService
from application.services.algorithm_service import SM2Service
from presentstion.schemas.card_schemas import CardBase


router = APIRouter()


@router.get("/card", tags=['card'])
async def get_cards(card_service: CardService = Depends(get_card_service)):
    """
    Возвращает все карточки.

    Returns:
        list[Card]: Все карточки.
    """
    return card_service.get_all_cards()


@router.get("/card/{card_id}", tags=['card'])
async def get_card(card_id: str, 
                   card_service: CardService = Depends(get_card_service)):
    """
    Возвращает карточку по id.

    Args:
        card_id (str): Уникальный идентификатор.

    Returns:
        Card: Карточка.
    """
    card = card_service.get_card_by_id(card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return card


@router.post("/card", tags=['card'])
async def post_card(card: CardBase, 
              card_service: CardService = Depends(get_card_service)):
    """
    Добавляет новую карточку.

    Args:
        new_card (Card): Тело новой карточки.

    Returns:
        Card: Добавленная карточка.
    """
    return card_service.add_card(card)


@router.put("/card/{card_id}", tags=['card'])
async def put_card(new_card: CardBase, 
             card_id: str,
             card_service: CardService = Depends(get_card_service)):
    """
    Заменяет параметры карточки.

    Args:
        card_id (str): Уникальный идентификатор карточки, которую необходимо изменить.
        new_card (Card): Тело карточки с обновленными параметрами.
    
    Returns:
        Card: Обновленная карточка.
    """
    return  card_service.change_card(card_id, new_card)


@router.delete("/card/{card_id}", tags=['card'])
async def del_card(card_id: str,
             card_service: CardService = Depends(get_card_service)):
    """
    Удаляет карточку.
    
    Args:
        card_id (str): Уникальный идентификатор карточки, которую необходимо изменить.
    
    Returns:
        Card: Удаленная картчочка.
    """
    return card_service.delete_card(card_id)


@router.post("/card/answer/{card_id}", tags=['card'])
async def post_answer(card_id: str, 
                quality: int, 
                algorithm_service: SM2Service = Depends(get_sm2_service)):
    """
    Получает ответ на карточку.
    
    Args:
        card_id (str): Уникальный идентификатор карточки.
        quality (int): Качество ответа от 0 до 5.
    
    Returns:
        Card: Обновленные параметры алгоритма для карточки.
    """
    new_params = algorithm_service.calculate_interval(card_id, quality)
    return new_params

