from fastapi import APIRouter, Depends, HTTPException

from presentstion.dependencies import get_deck_service
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


@router.post("/deck", tags=['deck'])
def post_deck(deck: DeckBase, 
              deck_service: DeckService = Depends(get_deck_service)):
    return deck_service.add_deck(deck)


@router.put("/deck/{deck_id}", tags=['deck'])
def put_deck(new_deck: DeckBase, 
             deck_id: str,
             deck_service: DeckService = Depends(get_deck_service)):
    return  deck_service.change_deck(deck_id, new_deck)


@router.delete("/deck/{deck_id}", tags=['deck'])
def del_deck(deck_id: str,
             deck_service: DeckService = Depends(get_deck_service)):
    return deck_service.delete_deck(deck_id)
