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
        print("(1) New Game")
        print("(2) Load Game")
        print("(exit) Exit")
        print()
        
        self.update_input()

        # self._state_list.append(GameState(self._state_list))

    def update_input(self) -> None:
        print("Input: ")
        
        input_str = ""
        try:
            input_str = int(input())
        except Exception as e:
            print(e)
            pass

        if input_str.isdigit(): 
            if input_str == "1":
                self._state_list.append(GameState(self._state_list))
            if input_str == "2":
                self._state_list.append(GameState(self._state_list))
            elif input_str == "exit":
                self._state_list.pop()
        else:
            print("input was not a number, please try again.")