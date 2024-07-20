import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions for fullscreen
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Random Circles")

# Colors
BLACK = (0, 0, 0)

# Circle class
class Circle:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.radius = random.randint(20, 100)
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
    
    def update(self):
        self.radius -= 1

# Game loop
circles = []
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            else:
                circles.append(Circle())
    
    for circle in circles[:]:
        if circle.radius > 0:
            circle.update()
            circle.draw(screen)
        else:
            circles.remove(circle)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()