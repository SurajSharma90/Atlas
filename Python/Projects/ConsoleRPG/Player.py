from collections import defaultdict
from Utils.Component import COMPONENT_TYPES
from Utils.LevelComponent import LevelComponent


class Player:
    def __init__(self, name):
        self.name = "default"
        self.components = {}
        self.init_components()
    
    def init_components(self):
        self.components[COMPONENT_TYPES.LEVEL_COMPONENT] = LevelComponent()

    def update(self):
        print(self.name)
