from States.State import State, StateTypes
from dataclasses import dataclass
from enum import Enum
from Utils.Systems.MenuSystem import MenuSystem
from Utils.InputValidation import get_input_int
from Entities.Player import Player
from States.CharacterCreatorState import CharacterCreatorState
from Utils.InputUtils import pause_continue
from Utils.Components.Component import ComponentTypes


class MenuOptions(Enum):
    TRAVEL_MENU="Travel Menu"
    CHARACTER_MENU="Character Menu"
    LIST_CHARACTERS="List Characters"
    SELECT_CHARACTER="Select Character"
    EXIT="Exit"

@dataclass
class GameState(State):
    _menu_system: MenuSystem
    _characters: list[Player]
    _active_character: Player

    def __init__(self, state_list: list) -> None:
        super().__init__(name=StateTypes.GAME_STATE.value, state_list=state_list)
        self._menu_system = MenuSystem()
        self._characters = []
        self._active_character = None
        self.init_menu()

    def init_menu(self) -> None:
        self._menu_system.add_option(option=MenuOptions.TRAVEL_MENU.value, number=1)
        self._menu_system.add_option(option=MenuOptions.CHARACTER_MENU.value, number=2)
        self._menu_system.add_option(option=MenuOptions.LIST_CHARACTERS.value, number=3)
        self._menu_system.add_option(option=MenuOptions.SELECT_CHARACTER.value, number=4)
        self._menu_system.add_option(option=MenuOptions.EXIT.value, number=0)

    def render_menu(self) -> None:
        self._menu_system.render()

    def render_active_player(self) -> None:
        if self._active_character != None:
            print(f"[ Selected Character: {self._active_character._name} | Level: {self._active_character.get_component(type=ComponentTypes.LEVEL_COMPONENT).get_level()} {self._active_character.get_component(type=ComponentTypes.LEVEL_COMPONENT).get_exp_bar(length=10)} ]")

    def update(self) -> None:
        super().update()
        self.render_active_player()
        self.render_menu()
        self.update_input()

    def update_input(self) -> None:
        input_int = get_input_int(prompt="Input: ")

        if(input_int != None):
            if input_int == self._menu_system.get(MenuOptions.TRAVEL_MENU.value):
                pass
            if input_int == self._menu_system.get(MenuOptions.CHARACTER_MENU.value):
                self._state_list.append(CharacterCreatorState(state_list=self._state_list, character_list=self._characters))
            if input_int == self._menu_system.get(MenuOptions.LIST_CHARACTERS.value):
                self.list_characters()
            if input_int == self._menu_system.get(MenuOptions.SELECT_CHARACTER.value):
                self.select_character()
            elif input_int == self._menu_system.get(MenuOptions.EXIT.value):
                self._state_list.pop()
        else:
            print("Wrong input! Try again.")
            pause_continue()
    
    def list_characters(self, start:int = 1, pause:bool = True) -> None:
        nr = start
        for character in self._characters:
            print(f"{nr}: {character._name}")
            nr += 1
        if pause == True:
            pause_continue()
    
    def select_character(self) -> None:
        self.list_characters(start=0, pause=False)
        if len(self._characters) > 0:
            index = get_input_int("Character index: ")
            if index >= 0 and index < len(self._characters):
                self._active_character = self._characters[index]
                print(f"Character {self._active_character._name} selected!")
            else:
                print("Invalid index. Please try again.")
        else:
            print("No characters. Please create some first.")
            
        pause_continue()
