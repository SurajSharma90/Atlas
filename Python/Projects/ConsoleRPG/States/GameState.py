from States.State import State, STATES
from dataclasses import dataclass
from enum import Enum
from Utils.Systems.MenuSystem import MenuSystem
from Utils.InputValidation import get_input_int
from Entities.Player import Player
from States.CharacterCreatorState import CharacterCreatorState


class MenuOptions(Enum):
    TRAVEL_MENU="Travel Menu"
    CHARACTER_MENU="Character Menu"
    EXIT="Exit"

@dataclass
class GameState(State):
    _menu_system: MenuSystem
    _characters: list[Player]
    _active_character: Player

    def __init__(self, state_list: list) -> None:
        super().__init__(name=STATES.GAME_STATE.value, state_list=state_list)
        self._menu_system = MenuSystem()
        self._characters = []
        self._active_character = None
        self.init_menu()

    def init_menu(self) -> None:
        self._menu_system.add_option(option=MenuOptions.TRAVEL_MENU.value, number=1)
        self._menu_system.add_option(option=MenuOptions.CHARACTER_MENU.value, number=2)
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
            if input_int == self._menu_system.get(MenuOptions.TRAVEL_MENU.value):
                pass
            if input_int == self._menu_system.get(MenuOptions.CHARACTER_MENU.value):
                self._state_list.append(CharacterCreatorState(state_list=self._state_list, character_list=self._characters))
            elif input_int == self._menu_system.get(MenuOptions.EXIT.value):
                self._state_list.pop()
        else:
            print("Wrong input! Try again.")