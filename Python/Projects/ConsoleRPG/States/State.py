import json
from dataclasses import dataclass
from enum import Enum


class STATES(Enum):
    MAIN_MENU_STATE = "main_menu_state"
    GAME_STATE = "game_state"
    TRAVEL_STATE = "travel_state"
    CHARACTER_CREATOR_STATE = "character_creator_state"

@dataclass
class State:
    _name: str
    _metadata: json
    _state_list: list

    def __init__(self, name: str, state_list: list) -> None:
        self._name = name
        self._state_list = state_list
        with open("Python/Projects/ConsoleRPG/metadata.json", 'r') as metadata_file:
            self._metadata = json.load(metadata_file)

    def update(self) -> None:
        print("==========" + self._metadata["metadata"][self._name]["title"] + "==========")
