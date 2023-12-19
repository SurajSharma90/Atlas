from dataclasses import dataclass
from Utils.Component import Component, COMPONENT_TYPES
from math import pow, sqrt


@dataclass 
class LevelComponent(Component):
    _level: int
    _exp: int
    _exp_next: int
    
    def __init__(self):
        super().__init__(COMPONENT_TYPES.LEVEL_COMPONENT)
        self._level = 1
        self._exp = 0
        self._exp_next = self.calculate_exp_next(2)

    def can_level_up(self) -> bool:
        return self._exp >= self._exp_next

    def level_up(self):
        if self._exp >= self._exp_next:
            self._level += 1
            self._exp -= self._exp_next
            self._exp_next = self.calculate_exp_next(self._level + 1)

            if self._exp < 0:
                self._exp = 0
                raise(Exception("Exp went below zero."))
    
    def calculate_exp_next(self, level: int) -> int:
        return int((((50*pow(level, 3))-(150*pow(level, 2))+(400*level))/3))
    
    def gain_exp(self, exp: int):
        
        self._exp += exp

        while self.can_level_up():
            self.level_up()
