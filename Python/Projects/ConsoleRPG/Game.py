from States.MainMenuState import MainMenuState
from States.State import State
from dataclasses import dataclass

@dataclass
class Game:
    _running: bool
    _states: list[State]
    _active_state: State = None

    def __init__(self):
        self._running = True
        self._states = []
        self._states.insert(0, MainMenuState(state_list=self._states))
        self._active_state = self._states[0]

    def update(self):
        self._active_state = self._states[len(self._states)-1]
        self._active_state.update()

    def run(self):
        while len(self._states) > 0:
            self.update()
            