from fastapi import FastAPI

from schemas import Card, CardBase, UpdatedParameter

cards = [
    {"id": "0", "name": "hello", "description": "привет"}, 
    {"id": "1", "name": "world", "description": "мир"}
]


app = FastAPI()


@app.get("/card")
async def get_cards():
    return cards


@app.post("/card")
async def add_card(card: CardBase):
    card = Card(
        id=str(len(cards)), 
        name=card.name, 
        description=card.description
    )
    cards.append(card.model_dump())
    return card


@app.get("/card/{card_id}")
async def get_card(card_id: str):
    res = next(filter(lambda card: card["id"] == card_id, cards))
    return res


@app.put("/card/{card_id}")
async def change_card(card_id: str, updated_card: CardBase):
    card = next(filter(lambda card: card["id"] == card_id, cards))
    card["name"] = updated_card.name
    card["description"] = updated_card.description
    return card
    

@app.patch("/patch/{card_id}")
async def patch_card(card_id: str, data: UpdatedParameter):
    card = next(filter(lambda card: card["id"] == card_id, cards))
    card[data.parameter] = data.value
    return card


@app.delete("/delete/{card_id}")
async def delete_card(card_id: str):
    #card = next(filter(lambda card: card["id"] == card_id, cards))
    return cards.pop(int(card_id))

