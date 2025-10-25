from pydantic import BaseModel
from typing import Any


class CardBase(BaseModel):
    name: str
    description: str
    # interval: float 
    # ef: float
    # quality: int


class CardSh(CardBase):
    id: str


class UpdatedParameter(BaseModel):
    parameter: str
    value: Any
