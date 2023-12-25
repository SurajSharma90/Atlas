from dataclasses import dataclass
from Entities.Entity import Entity
from Utils.Components.Component import ComponentTypes
from Utils.Components.LevelComponent import LevelComponent
from Utils.Components.AttributeComponent import AttributeComponent


@dataclass
class Player(Entity):
    _name: str
    
    def __init__(self, name) -> None:
        super().__init__()
        self._name = name
        self.init_components()
    
    def init_components(self) -> None:
        self.add_component(LevelComponent())
        self.add_component(AttributeComponent())

    def update(self) -> None:
        print(self._name)
    
    def get_character_sheet(self) -> str:
        print(f"[ Character Sheet for: {self._name} ]")
        print(f" * Level: {self.get_component(ComponentTypes.LEVEL_COMPONENT).get_level()}")
        print(f" * Experience: {self.get_component(ComponentTypes.LEVEL_COMPONENT).get_exp()} / {self.get_component(ComponentTypes.LEVEL_COMPONENT).get_exp_next()}")
        print(f" * {self.get_component(ComponentTypes.LEVEL_COMPONENT).get_exp_bar()}")
        print("=========================")
        #print({self.get_component(ComponentTypes.ATTRIBUTE_COMPONENT)})
