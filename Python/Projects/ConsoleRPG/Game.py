from Player import Player
from State import State, StateTypes


class Game:
    def __init__(self):
        self.running = True
        self.player = Player("None")
        self.states = []
        self.states.insert(0, State(StateTypes.MAIN_MENU))
        self.active_state = self.states[0]

    def update(self):
        self.active_state.update()

    def run(self):
        while self.running:
            print("Input: ")
            input_str = input()
            if input_str == "exit":
                self.running = False
                break

            self.update()
