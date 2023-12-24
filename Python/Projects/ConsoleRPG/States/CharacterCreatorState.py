from States.State import State, StateTypes
from dataclasses import dataclass
from enum import Enum
from Utils.Systems.MenuSystem import MenuSystem
from Utils.InputValidation import get_input_int
from Entities.Player import Player
from Utils.InputUtils import pause_continue


class MenuOptions(Enum):
    NEW_CHARACTER="New Character"
    DELETE_CHARACTER="Delete Character"
    LIST_CHARACTERS="List Characters"
    EXIT="Exit"

@dataclass
class CharacterCreatorState(State):
    _menu_system: MenuSystem
    _characters: list[Player]

    def __init__(self, state_list: list, character_list: list[Player]) -> None:
        super().__init__(name=StateTypes.CHARACTER_CREATOR_STATE.value, state_list=state_list)
        self._menu_system = MenuSystem()
        self._characters = character_list
        self.init_menu()

    def init_menu(self) -> None:
        self._menu_system.add_option(option=MenuOptions.NEW_CHARACTER.value, number=1)
        self._menu_system.add_option(option=MenuOptions.DELETE_CHARACTER.value, number=2)
        self._menu_system.add_option(option=MenuOptions.LIST_CHARACTERS.value, number=3)
        self._menu_system.add_option(option=MenuOptions.EXIT.value, number=0)

    def render_menu(self) -> None:
        self._menu_system.render()

    def update(self) -> None:
        super().update()        
        self.render_menu()
        self.update_input()

    def update_input(self) -> None:
        input_int = get_input_int(prompt="Input: ")

        if(input_int != None):
            if input_int == self._menu_system.get(MenuOptions.NEW_CHARACTER.value):
                self.create_character()
            if input_int == self._menu_system.get(MenuOptions.DELETE_CHARACTER.value):
                pass
            if input_int == self._menu_system.get(MenuOptions.LIST_CHARACTERS.value):
                self.list_characters()
            elif input_int == self._menu_system.get(MenuOptions.EXIT.value):
                self._state_list.pop()
        else:
            print("Wrong input! Try again.")

    def create_character(self) -> None:
        print("Input Name: ")
        name = input()
        self._characters.append(Player(name=name))
        print(f"Character with name {name} created!")
        pause_continue()
    
    def list_characters(self) -> None:
        nr = 1
        for character in self._characters:
            print(f"{nr}: {character._name}")
            nr += 1
        pause_continue()