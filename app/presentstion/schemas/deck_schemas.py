from pydantic import BaseModel


class DeckBase(BaseModel):
    name: str
    algorithm: str


class DeckSh(DeckBase):
    id: str