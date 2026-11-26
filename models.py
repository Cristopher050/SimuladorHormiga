
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Ant:
    id: int
    x: float
    y: float
    carrying: bool = False


@dataclass(frozen=True)
class GameState:
    ants: Tuple[Ant, ...]
    delivered: int = 0
    frame: int = 0
