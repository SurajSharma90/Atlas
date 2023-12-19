from Player import Player
from States.MainMenuState import MainMenuState
from States.State import STATES
from States.GameState import GameState
import json


class Game:
    def __init__(self):
        self.running = True
        self.player = Player("None")
        self.states = []
        self.states.insert(0, MainMenuState(state_list=self.states))
        self.active_state = self.states[0]

    def update(self):
        self.active_state = self.states[len(self.states)-1]
        self.active_state.update()

    def run(self):
        while len(self.states) > 0:
            self.update()

            print("Input: ")
            input_str = input()
            if input_str == "exit":
                self.states.pop()
                print("del")
                    
            print(len(self.states))
            