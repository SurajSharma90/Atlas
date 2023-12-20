from dataclasses import dataclass
from Utils.Components.Component import COMPONENT_TYPES, Component
from enum import Enum


@dataclass
class Entity:
    _components: dict
    
    def __init__(self) -> None:
        self._components = {}
    
    def add_component(self, component: Component) -> None:
        self._components[type(component)] = component
        
    def get_component(self, type: Enum) -> Component:
        return self._components[type]
        
