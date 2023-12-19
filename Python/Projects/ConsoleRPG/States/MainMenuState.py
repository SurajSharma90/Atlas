from dataclasses import dataclass
from enum import Enum
from States.State import State, STATES
from States.GameState import GameState

#Import from other folder
# import sys
# sys.path.insert(1, '../../ConsoleRPG')
# import Utils.Component
# Run from __main__ and all modules will be found!


@dataclass
class MainMenuState(State):
    def __init__(self, state_list: list) -> None:
        super().__init__(name=STATES.MAIN_MENU_STATE.value, state_list=state_list)

    def update(self) -> None:
        super().update()
        print("(1) Play Game")
        print("(exit) Exit")
        print()

        # self._state_list.append(GameState(self._state_list))

