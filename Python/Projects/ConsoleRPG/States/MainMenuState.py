from States.State import State


class MainMenuState(State):
    def __init__(self):
        super().__init__()

    def update(self):
        print("From Main Menu")