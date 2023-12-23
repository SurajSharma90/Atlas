from dataclasses import dataclass
from enum import Enum
from States.State import State, STATES
from States.GameState import GameState
from Utils.Systems.MenuSystem import MenuSystem
from Utils.InputValidation import get_input_int

#Import from other folder
# import sys
# sys.path.insert(1, '../../ConsoleRPG')
# import Utils.Component
# Run from __main__ and all modules will be found!

class MenuOptions(Enum):
    NEW_GAME="New Game"
    LOAD_GAME="Load Game"
    EXIT="Exit"


@dataclass
class MainMenuState(State):
    _menu_system: MenuSystem

    def __init__(self, state_list: list) -> None:
        super().__init__(name=STATES.MAIN_MENU_STATE.value, state_list=state_list)
        self._menu_system = MenuSystem()
        self.init_menu()

    def init_menu(self) -> None:
        self._menu_system.add_option(option=MenuOptions.NEW_GAME.value, number=1)
        self._menu_system.add_option(option=MenuOptions.LOAD_GAME.value, number=2)
        self._menu_system.add_option(option=MenuOptions.EXIT.value, number=0)

    def render_menu(self) -> None:
        self._menu_system.render()

    def update(self) -> None:
        super().update()
        
        self.render_menu()
        self.update_input()

        # self._state_list.append(GameState(self._state_list))

    def update_input(self) -> None:

        input_int = get_input_int(prompt="Input: ")

        if(input_int != None):
            if input_int == self._menu_system.get(MenuOptions.NEW_GAME.value):
                self._state_list.append(GameState(self._state_list))
            if input_int == self._menu_system.get(MenuOptions.LOAD_GAME.value):
                self._state_list.append(GameState(self._state_list))
            elif input_int == self._menu_system.get(MenuOptions.EXIT.value):
                self._state_list.pop()
        else:
            print("Wrong input! Try again.")