from States.State import State, STATES


class GameState(State):
    def __init__(self, state_list: list) -> None:
        super().__init__(name=STATES.GAME_STATE.value, state_list=state_list)
