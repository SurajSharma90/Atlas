import pygame
from Circle import Circle
from VectorMath import Vectorf, Vector2f

pygame.init()

SCREEN_DIMENSIONS = {"x": 1920, "y": 1080}
POINT_RADIUS = 10
LABEL_RADIUS = 5

display = pygame.display
screen = display.set_mode((SCREEN_DIMENSIONS["x"], SCREEN_DIMENSIONS["y"]))
display.set_caption("Simple Window")

points: [Circle] = []
labels: [Circle] = []
"""
points.append(Circle(Vector2f(50.0, 50.0), POINT_RADIUS, pygame.Color(255, 0, 0, 255)))
points.append(Circle(Vector2f(120.0, 120.0), POINT_RADIUS, pygame.Color(255, 0, 0, 255)))

vectorab=Vectorf(points[0].point, points[1].point)
point_label = (points[0].point + vectorab)

labels.append(Circle(point_label, LABEL_RADIUS, pygame.Color(0, 0, 255, 255)))
"""
create = True

running = True

def add_label(labels: [Circle], points: [Circle]):
    
    if len(points) > 0:
        if len(points) == 1:
            labels.append(
                Circle(
                    Vector2f(points[0].point.x, points[0].point.y - POINT_RADIUS*2),
                    LABEL_RADIUS,
                    pygame.Color(0, 0, 255, 255),
                )
            )
        elif len(points) > 1:
            last_point = points[len(points)-1].point
            nearest_neighbor = points[len(points)-2].point
            vec = points[len(points)-2].point + Vectorf(points[len(points) - 2].point, points[len(points) - 1].point)
            print(last_point.x, nearest_neighbor.x)
            
            mean_point = 0
            posx = 0
            posy = 0
            labels.append(
                Circle(
                    Vector2f(vec.x, vec.y),
                    LABEL_RADIUS,
                    pygame.Color(0, 0, 255, 255),
                )
            )

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
                        POINT_RADIUS,
                        pygame.Color(255, 0, 0, 255),
                    )
                )
                add_label(labels=labels, points=points)
                # print("You pressed the left mouse button at (%d, %d)" % event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            create = True

    screen.fill((0, 0, 0))

    for point in points:
        point.render(screen)
    for label in labels:
        label.render(screen)

    display.update()

pygame.quit()
