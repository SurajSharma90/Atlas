from dataclasses import dataclass
import argparse
from operator import indexOf


@dataclass
class MenuSystem:
    _options: dict[str, int]

    def __init__(self) -> None:
        self._options = {}

    def add_option(self, option: str, number: int) -> None:
        if option in self._options:
            print("Option already exists!")
        else:
            self._options[option] = number
    
    def remove_option(self, option: str) -> None:
        if option in self._options:
            del self._options[option]
        else:
            print("Option does not exist!")

    def get(self, option: str) -> int:
        return self._options[option]

    def render(self) -> None:
        for key in self._options:
            print(f"[{self._options[key]}] - {key}")
        print("")
