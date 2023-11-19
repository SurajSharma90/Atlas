import pygame

import Room


class Game:
    def __init__(self):
        self.running = True
        self.window = None
        self.display = None
        self.rooms = []

        self.init_window(1920, 1080)

    def init_window(self, x, y):
        self.display = pygame.display
        self.window = self.display.set_mode((x, y))

    def render(self):
        self.window.fill((0, 0, 0))
        self.display.update()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.render()

        pygame.quit()
