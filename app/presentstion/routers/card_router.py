from fastapi import APIRouter, Depends, HTTPException

from presentstion.dependencies import get_card_service, get_sm2_service
from application.services.card_service import CardService, SM2Service
from presentstion.schemas.schemas import CardSh, CardBase


router = APIRouter()


@router.get("/card")
async def get_cards(card_service: CardService = Depends(get_card_service)):
    return card_service.get_all_cards()


@router.get("/card/{card_id}")
async def get_card(card_id: str, 
                   card_service: CardService = Depends(get_card_service)):
    card = card_service.get_card_by_id(card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return card


@router.post("/card")
def post_card(card: CardBase, 
              card_service: CardService = Depends(get_card_service)):
    card_service.add_card(card)
    return card


@router.put("/card")
def put_card(new_card: CardBase, 
             card_id: str,
             card_service: CardService = Depends(get_card_service)):
    return  card_service.change_card(card_id, new_card)


@router.delete("/card")
def del_card(card_id: str,
             card_service: CardService = Depends(get_card_service)):
    return card_service.delete_card(card_id)


@router.post("/card/answer")
def post_answer(card: CardSh, 
                quality: int, 
                card_service: CardService = Depends(get_card_service),
                algorithm_service: SM2Service = Depends(get_sm2_service)):
    card_new = algorithm_service.calculate_interval(card, quality)
    return card_service.change_card(card_new.id, card_new)

