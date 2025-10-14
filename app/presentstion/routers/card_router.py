from fastapi import APIRouter, Depends

from presentstion.dependencies import get_card_service
from application.services.card_service import CardService
from presentstion.schemas.schemas import Card, CardBase, UpdatedParameter

router = APIRouter()


@router.get("/card")
async def get_cards(card_service: CardService = Depends(get_card_service)):
    return card_service.get_all_cards()


# @router.post("/card")
# async def add_card(card: CardBase):
#     card = Card(
#         id=str(len(cards)), 
#         name=card.name, 
#         description=card.description
#     )
#     cards.append(card.model_dump())
#     return card


# @router.get("/card/{card_id}")
# async def get_card(card_id: str):
#     res = next(filter(lambda card: card["id"] == card_id, cards))
#     return res


# @router.put("/card/{card_id}")
# async def change_card(card_id: str, updated_card: CardBase):
#     card = next(filter(lambda card: card["id"] == card_id, cards))
#     card["name"] = updated_card.name
#     card["description"] = updated_card.description
#     return card
    

# @router.patch("/patch/{card_id}")
# async def patch_card(card_id: str, data: UpdatedParameter):
#     card = next(filter(lambda card: card["id"] == card_id, cards))
#     card[data.parameter] = data.value
#     return card


# @router.delete("/delete/{card_id}")
# async def delete_card(card_id: str):
#     card = next(filter(lambda card: card["id"] == card_id, cards))
#     card_dict_id = cards.index(card)
#     return cards.pop(card_dict_id)
