from dataclasses import dataclass


@dataclass
class CombatSystem:
    queue: list
    turn_index: int

    def __init__(self):
        self.queue = []
        self.turn_index = 0

    def add_to_queue(self, list):
        for object in list:
            self.queue.append(object)

    def switch_turn(self):
        if len(self.queue) > 1:
            if self.turn_index < len(self.queue) - 1:
                self.turn_index += 1
            else:
                self.turn_index = 0
    
    def get_turn_object(self):
        return self.queue[self.turn_index]

    def _print_queue(self):
        print(self.queue)
