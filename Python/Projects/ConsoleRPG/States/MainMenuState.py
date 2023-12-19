from dataclasses import dataclass
from enum import Enum
from States.State import State, STATES
from States.GameState import GameState


@dataclass
class MainMenuState(State):
    def __init__(self, state_list: list) -> None:
        super().__init__(name=STATES.MAIN_MENU_STATE.value, state_list=state_list)

    def update(self) -> None:
        super().update()
        print("(1) Play Game")
        print("(exit) Exit")
        print()
