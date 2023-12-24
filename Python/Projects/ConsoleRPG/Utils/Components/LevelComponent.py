from dataclasses import dataclass
from Utils.Components.Component import Component, ComponentTypes
from math import pow, sqrt, floor


@dataclass 
class LevelComponent(Component):
    _level: int
    _exp: int
    _exp_next: int
    
    def __init__(self) -> None:
        super().__init__(ComponentTypes.LEVEL_COMPONENT)
        self._level = 1
        self._exp = 0
        self._exp_next = self.calculate_exp_next(2)

    def can_level_up(self) -> bool:
        return self._exp >= self._exp_next

    def level_up(self) -> None:
        if self._exp >= self._exp_next:
            self._level += 1
            self._exp -= self._exp_next
            self._exp_next = self.calculate_exp_next(self._level + 1)

            if self._exp < 0:
                self._exp = 0
                raise(Exception("Exp went below zero."))
    
    def calculate_exp_next(self, level: int) -> int:
        return int((((50*pow(level, 3))-(150*pow(level, 2))+(400*level))/3))
    
    def gain_exp(self, exp: int) -> None:
        
        self._exp += exp

        while self.can_level_up():
            self.level_up()
    
    def get_level(self) -> int:
        return self._level
    
    def get_exp(self) -> int:
        return self._exp
    
    def get_exp_next(self) -> int:
        return self._exp_next

    def get_exp_bar(self, length:int=10, fill:str = "=", empty:str = "-", start:str = "[", end:str = "]") -> str:
        percent_fill = self._exp / self._exp_next
        percent_empty = 1.0 - percent_fill
        exp_bar = f"{start}{fill*floor(length*percent_fill)}{empty*floor(length*percent_empty)}{end}"
        return exp_bar
    