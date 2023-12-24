from dataclasses import dataclass
from Entities.Entity import Entity
from Utils.Components.Component import ComponentTypes
from Utils.Components.LevelComponent import LevelComponent
from Utils.Components.AttributeComponent import AttributeComponent


@dataclass
class Player(Entity):
    _name: str
    
    def __init__(self, name):
        super().__init__()
        self._name = name
        self.init_components()
    
    def init_components(self):
        self.add_component(LevelComponent())
        self.add_component(AttributeComponent())

    def update(self):
        print(self._name)
