from Player import Player
from States.MainMenuState import MainMenuState


class Game:
    def __init__(self):
        self.running = True
        self.player = Player("None")
        self.states = []
        self.states.insert(0, MainMenuState())
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
