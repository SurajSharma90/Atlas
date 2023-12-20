from States.State import State, STATES
from Utils.Systems.CombatSystem import CombatSystem


class GameState(State):
    def __init__(self, state_list: list) -> None:
        super().__init__(name=STATES.GAME_STATE.value, state_list=state_list)

    def update(self) -> None:
        super().update()
        print("(1) Travel")
        print("(exit) Exit")
        print()
        
        self.update_input()

        # self._state_list.append(GameState(self._state_list))

    def update_input(self) -> None:
        print("Input: ")
        input_str = input()
        if input_str == "exit":
            self._state_list.pop()