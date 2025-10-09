from pydantic import BaseModel
from typing import Any

class CardBase(BaseModel):
    name: str
    description: str


class Card(CardBase):
    id: str


class UpdatedParameter(BaseModel):
    parameter: str
    value: Any
