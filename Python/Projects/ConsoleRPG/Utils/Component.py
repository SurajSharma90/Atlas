from dataclasses import dataclass
from enum import Enum


class COMPONENT_TYPES(Enum):
    LEVEL_COMPONENT = "level_component"

@dataclass 
class Component:
    _type: COMPONENT_TYPES

    def is_component(self, type):
        return self._type == type