from dataclasses import dataclass
import argparse


@dataclass
class MenuSystem:
    _options: dict

    def __init__(self) -> None:
        self._options = {}

    def add_option(self, identifier: str, function: function) -> None:
        self._options[identifier] = function
    
    def execute_option(self, identifier: str, function: function, args: list) -> None:
        self._options[identifier](args)
