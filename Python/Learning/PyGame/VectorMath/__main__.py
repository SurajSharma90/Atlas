import pygame
from Circle import Circle
from VectorMath import Vectorf, Vector2f

pygame.init()

SCREEN_DIMENSIONS = {"x": 1920, "y": 1080}

display = pygame.display
screen = display.set_mode((SCREEN_DIMENSIONS["x"], SCREEN_DIMENSIONS["y"]))
display.set_caption("Simple Window")

points: [Circle] = []
labels: [Circle] = []
points.append(Circle(Vector2f(50.0, 50.0), 20, pygame.Color(255, 0, 0, 255)))
create = True

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if create == True:
                create = False
                points.append(
                    Circle(
                        Vector2f(event.pos[0], event.pos[1]),
                        20,
                        pygame.Color(255, 0, 0, 255),
                    )
                )
                # print("You pressed the left mouse button at (%d, %d)" % event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            create = True

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        rect.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        rect.move_ip(1, 0)
    if key[pygame.K_w] == True:
        rect.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        rect.move_ip(0, 1)

    screen.fill((0, 0, 0))

    for point in points:
        point.render(screen)

    display.update()

pygame.quit()
