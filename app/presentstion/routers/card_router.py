from fastapi import APIRouter, Depends, HTTPException

from domain.entities.sm2_params import SM2Params
from presentstion.dependencies import get_card_service, get_sm2_service
from application.services.card_service import CardService, SM2Service
from presentstion.schemas.schemas import CardSh, CardBase


router = APIRouter()


@router.get("/card", tags=['card'])
async def get_cards(card_service: CardService = Depends(get_card_service)):
    return card_service.get_all_cards()


@router.get("/card/{card_id}", tags=['card'])
async def get_card(card_id: str, 
                   card_service: CardService = Depends(get_card_service)):
    card = card_service.get_card_by_id(card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return card


@router.post("/card", tags=['card'])
def post_card(card: CardBase, 
              card_service: CardService = Depends(get_card_service)):
    return card_service.add_card(card)


@router.put("/card", tags=['card'])
def put_card(new_card: CardBase, 
             card_id: str,
             card_service: CardService = Depends(get_card_service)):
    return  card_service.change_card(card_id, new_card)


@router.delete("/card", tags=['card'])
def del_card(card_id: str,
             card_service: CardService = Depends(get_card_service)):
    return card_service.delete_card(card_id)


@router.post("/card/answer", tags=['card'])
def post_answer(card_id: str, 
                quality: int, 
                algorithm_service: SM2Service = Depends(get_sm2_service)):
    new_params = algorithm_service.calculate_interval(card_id, quality)
    return new_params

