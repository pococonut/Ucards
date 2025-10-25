from dataclasses import dataclass


@dataclass
class SM2Params:
    id: str
    interval: float = 1
    ef: float = 2.5
    quality: int = 1