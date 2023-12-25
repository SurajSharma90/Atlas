from dataclasses import dataclass
import pygame

@dataclass
class ScreenSize:
    x: int
    y: int

@dataclass
class Game:
    _surface_dimensions: ScreenSize
    _display: pygame.display
    _surface: pygame.surface
    _running: bool

    def __init__(self):
        pygame.init()
        self._surface_dimensions = ScreenSize(x=800, y=600)
        self._running = True
        self.init_window()

    def init_window(self):
        self._display = pygame.display
        self._surface = self._display.set_mode((self._surface_dimensions.x, self._surface_dimensions.y))
        self._display.set_caption("Ubongo!")

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

                key = pygame.key.get_pressed()
                if key[pygame.K_a] == True:
                    print("A")
                elif key[pygame.K_d] == True:
                    print("D")
                if key[pygame.K_w] == True:
                    print("W")
                elif key[pygame.K_s] == True:
                    print("S")

    def render(self):
        self._surface.fill((0, 0, 0))

        self._display.update()


    def run(self):
        while self._running:
            
            self.update()

            self.render()
