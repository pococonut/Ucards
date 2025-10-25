from dataclasses import dataclass


@dataclass
class SM2Params:
    id: str
    interval: float
    ef: float
    quality: int