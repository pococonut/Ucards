from dataclasses import dataclass


@dataclass
class Card:
    id: str
    name: str
    description: str
    next_review: int 
    level: str
