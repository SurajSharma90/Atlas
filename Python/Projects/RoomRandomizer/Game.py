import pygame

import Room

class Game:
    def __init__(self):
        self.running = True
        self.window = None
        self.display = None
        self.rooms = []
        
        self.InitWindow(1920, 1080)
    
    def InitWindow(self, x, y):
        self.display = pygame.display
        self.window = self.display.set_mode((x, y))
        
    def Render(self):
        self.window.fill((0,0,0))
        self.display.update()
    
    def Run(self):
        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.Render()
            
        pygame.quit()