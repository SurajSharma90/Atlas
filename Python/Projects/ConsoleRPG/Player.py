from Utils.Component import COMPONENT_TYPES
from Utils.LevelComponent import LevelComponent
from Utils.AttributeComponent import AttributeComponent


class Player:
    def __init__(self, name):
        self.name = "default"
        self.components = {}
        self.init_components()
    
    def init_components(self):
        self.components[COMPONENT_TYPES.LEVEL_COMPONENT] = LevelComponent()
        self.components[COMPONENT_TYPES.ATTRIBUTE_COMPONENT] = AttributeComponent()

    def update(self):
        print(self.name)
