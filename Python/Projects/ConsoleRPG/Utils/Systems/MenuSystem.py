from dataclasses import dataclass
import argparse
from operator import indexOf


@dataclass
class MenuSystem:
    _options: dict[str, int]

    def __init__(self) -> None:
        self._options = {}

    def add_option(self, option: str) -> None:
        if option in self._options:
            print("Option already exists!")
        else:
            option_nr = len(self._options)+1
            self._options[option] = option_nr
    
    def remove_option(self, option: str) -> None:
        if option in self._options:
            del self._options[option]
        else:
            print("Option does not exist!")

    def render(self) -> None:
        for key in self._options:
            print(f"[{self._options[key]}] - {key}\n")
