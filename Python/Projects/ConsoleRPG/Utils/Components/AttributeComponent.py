from dataclasses import dataclass
from Utils.Components.Component import Component, COMPONENT_TYPES
from enum import Enum


class ATTRIBUTE_TYPES(Enum):
    STR="Strength"
    VIT="Vitality"
    DEX="Dexterity"
    AGI="Agility"
    INT="Intelligence"
    LUC="Luck"

@dataclass 
class AttributeComponent(Component):
    _skillpoints: int
    _attributes: dict
    
    def __init__(self, skillpoints: int = 5) -> None:
        super().__init__(COMPONENT_TYPES.ATTRIBUTE_COMPONENT)
        self._skillpoints = skillpoints
        
        self._attributes = {
            ATTRIBUTE_TYPES.STR: 1,
            ATTRIBUTE_TYPES.VIT: 1,
            ATTRIBUTE_TYPES.DEX: 1,
            ATTRIBUTE_TYPES.AGI: 1,
            ATTRIBUTE_TYPES.INT: 1,
            ATTRIBUTE_TYPES.LUC: 1,
        }

    def add_skillpoints(self, skillpoints: int) -> None:
        self._skillpoints = skillpoints

    def assign_skillpoint(self, attribute: Enum, skillpoints: int) -> None:
        if self._skillpoints > 0 and self._skillpoints >= skillpoints:
            self._attributes[attribute] += skillpoints
            self._skillpoints -= skillpoints
        else:
            print("Not enough attribute points to spend.")
    
    def get_attribute(self, type: Enum) -> int:
        return self._attributes[type]

    def _print_attributes(self) -> None:
        print(self._attributes)
