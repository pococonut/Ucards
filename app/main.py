from fastapi import FastAPI

from presentstion.routers import card_router, deck_router
from infrastructure.database.core.tables import metadata
from infrastructure.database.core.connection import engine


metadata.create_all(bind=engine)

app = FastAPI(title="Ucards")

app.include_router(deck_router.router)
app.include_router(card_router.router)
