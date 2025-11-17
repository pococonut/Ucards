from fastapi import FastAPI

from app.presentstion.routers import card_router, deck_router


app = FastAPI(title="Ucards")

app.include_router(deck_router.router)
app.include_router(card_router.router)
