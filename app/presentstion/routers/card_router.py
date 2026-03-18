from typing import Optional
from fastapi import APIRouter, Depends, HTTPException

from domain.entities.card import Card
from presentstion.mappers.alghorithm_mapper import SM2Mapper
from presentstion.mappers.card_mapper import CardMapper
from presentstion.schemas.algorithm_schemas import SM2Response
from presentstion.dependencies import get_user_use_cases
from application.services.card_service import CardService
from application.services.algorithm_service import SM2Service
from presentstion.schemas.card_schemas import CardBase, CardResponse


router = APIRouter()


@router.get("/card", tags=['card'])
async def get_cards(card_service: CardService = Depends(get_user_use_cases)) -> list[CardResponse]:
    """
    Возвращает все карточки.

    Returns:
        list[CardResponse]: Все карточки.
    """
    result: list[CardResponse] =  [CardMapper.to_response(card) for card in card_service.get_all_cards()]
    return result


@router.get("/card/{card_id}", tags=['card'])
async def get_card(card_id: str,
                   card_service: CardService = Depends(get_user_use_cases)) -> CardResponse:
    """
    Возвращает карточку по id.

    Args:
        card_id (str): Уникальный идентификатор.

    Returns:
        CardResponse: Карточка.
    """
    card: Optional[Card] = card_service.get_card_by_id(card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    
    response: CardResponse = CardMapper.to_response(card)
    return response


@router.post("/card", tags=['card'])
async def post_card(card: CardBase, 
                    card_service: CardService = Depends(get_user_use_cases)) -> CardResponse:
    """
    Добавляет новую карточку.

    Args:
        new_card (CardBase): Параметры новой карточки.

    Returns:
        CardResponse: Добавленная карточка.
    """
    result: CardResponse = CardMapper.to_response(card_service.add_card(card))
    return result


@router.put("/card/{card_id}", tags=['card'])
async def put_card(new_card: dict,
             card_id: str,
             card_service: CardService = Depends(get_user_use_cases)) -> CardResponse:
    """
    Заменяет параметры карточки.

    Args:
        card_id (str): Уникальный идентификатор карточки, которую необходимо изменить.
        new_card (Card): Тело карточки с обновленными параметрами.
    
    Returns:
        CardResponse: Обновленная карточка.
    """
    result: CardResponse = CardMapper.to_response(card_service.change_card(card_id, new_card))
    return result


@router.delete("/card/{card_id}", tags=['card'])
async def del_card(card_id: str,
                   card_service: CardService = Depends(get_user_use_cases)) -> bool:
    """
    Удаляет карточку.
    
    Args:
        card_id (str): Уникальный идентификатор карточки, которую необходимо изменить.
    
    Returns:
        CardResponse: Удаленная картчочка.
    """
    result: bool = card_service.delete_card(card_id)
    return result


# @router.post("/card/answer/{card_id}", tags=['card'])
# async def post_answer(card_id: str,
#                 quality: int,
#                 algorithm_service: SM2Service = Depends(get_sm2_service)) -> SM2Response:
#     """
#     Получает ответ на карточку.
    
#     Args:
#         card_id (str): Уникальный идентификатор карточки.
#         quality (int): Качество ответа от 0 до 5.
    
#     Returns:
#         SM2Response: Обновленные параметры алгоритма для карточки.
#     """
#     result: SM2Response = SM2Mapper.to_response(algorithm_service.calculate_interval(card_id, quality))
#     return result

