from dataclasses import dataclass
from datetime import date


@dataclass
class SM2Params:
    id: str
    interval: float
    ef: float
    quality: int
    show_dt: date