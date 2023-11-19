import pygame
from Circle import Circle
from Polygon import Polygon
from Utils.VectorMath import Vector, Point

    
pygame.init()

SCREEN_DIMENSIONS = {"x": 1200, "y": 600}

display = pygame.display
screen = display.set_mode((SCREEN_DIMENSIONS["x"], SCREEN_DIMENSIONS["y"]))
display.set_caption("Simple Window")

polygon = Polygon()

create = True

running = True

def update():
    global running, create

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if create == True:
                create = False
                polygon.add_point(Point(event.pos[0], event.pos[1]))
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            create = True

def render():
    screen.fill((0, 0, 0))
    polygon.render(screen)
    display.update()

def main():

    global running, create

    while running:
        update()
        render()

    pygame.quit()


if __name__ == "__main__":
    main()
