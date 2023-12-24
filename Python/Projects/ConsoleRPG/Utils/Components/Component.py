from dataclasses import dataclass
from enum import Enum


class ComponentTypes(Enum):
    LEVEL_COMPONENT = "level_component"
    ATTRIBUTE_COMPONENT = "attribute_component"

@dataclass 
class Component:
    _type: ComponentTypes

    def is_component(self, type):
        return self._type == type