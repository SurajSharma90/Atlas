from States.State import State


class GameState(State):
    def __init__(self):
        super().__init__()
    
    def update(self):
        print("From GameState")

