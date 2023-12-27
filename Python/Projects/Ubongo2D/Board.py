from pygame import Rect
from dataclasses import dataclass


@dataclass
class Board:
    cells: list[list[Rect]]