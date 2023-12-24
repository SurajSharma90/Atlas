from dataclasses import dataclass
from Utils.Components.Component import Component, ComponentTypes
from Utils.Components.LevelComponent import LevelComponent
from Utils.Components.AttributeComponent import AttributeComponent
from enum import Enum


@dataclass
class Entity:
    _components: dict
    
    def __init__(self) -> None:
        self._components = {}
    
    def add_component(self, component: Component) -> None:
        if isinstance(component, LevelComponent):
            self._components[ComponentTypes.LEVEL_COMPONENT] = component
        elif isinstance(component, AttributeComponent):
            self._components[ComponentTypes.ATTRIBUTE_COMPONENT] = component
        else:
            print("No component type matches with the one given!")
        
    def get_component(self, type: Enum) -> Component:
        return self._components[type]
        
