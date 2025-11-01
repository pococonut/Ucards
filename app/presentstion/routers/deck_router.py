from datetime import date
from fastapi import APIRouter, Depends, HTTPException

from domain.entities.algorithm import SM2Params
from application.services.algorithm_service import SM2Service
from presentstion.dependencies import get_deck_service, get_sm2_service
from application.services.deck_service import DeckService
from application.services.deck_service import DeckService
from presentstion.schemas.deck_schemas import DeckBase


router = APIRouter()


@router.get("/deck", tags=['deck'])
async def get_decks(deck_service: DeckService = Depends(get_deck_service)):
    return deck_service.get_all_decks()


@router.get("/deck/{deck_id}", tags=['deck'])
async def get_deck(deck_id: str, 
                   deck_service: DeckService = Depends(get_deck_service)):
    deck = deck_service.get_deck_by_id(deck_id)
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found")
    return deck


@router.get("/deck/{deck_id}/cards", tags=['deck'])
async def get_cards(deck_id: str,
              deck_service: DeckService = Depends(get_deck_service)):
    return deck_service.get_cards(deck_id)


@router.get("/deck/{deck_id}/learn", tags=['deck'])
async def get_cards(deck_id: str,
              deck_service: DeckService = Depends(get_deck_service),
              algorithm_service: SM2Service = Depends(get_sm2_service)):
    cards = deck_service.get_cards(deck_id)
    learning_cards = algorithm_service.get_learning_cards(cards)
    return learning_cards


@router.post("/deck", tags=['deck'])
async def post_deck(deck: DeckBase, 
              deck_service: DeckService = Depends(get_deck_service)):
    return deck_service.add_deck(deck)


@router.put("/deck/{deck_id}", tags=['deck'])
async def put_deck(new_deck: DeckBase, 
             deck_id: str,
             deck_service: DeckService = Depends(get_deck_service)):
    return  deck_service.change_deck(deck_id, new_deck)


@router.delete("/deck/{deck_id}", tags=['deck'])
async def del_deck(deck_id: str,
             deck_service: DeckService = Depends(get_deck_service)):
    return deck_service.delete_deck(deck_id)


