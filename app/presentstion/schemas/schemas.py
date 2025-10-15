from pydantic import BaseModel
from typing import Any


class CardBase(BaseModel):
    name: str
    description: str
    next_review: int
    level: str


class CardSh(CardBase):
    id: str


class UpdatedParameter(BaseModel):
    parameter: str
    value: Any
