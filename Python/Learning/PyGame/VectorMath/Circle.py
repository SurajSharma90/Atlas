import pygame
from VectorMath import Vector2f


class Circle:
    def __init__(self, point: Vector2f, radius: float, color: pygame.Color):
        self.point = point
        self.radius = radius
        self.color = color

    def render(self, screen: pygame.Surface):
        pygame.draw.circle(
            surface=screen,
            center=(self.point.x, self.point.y),
            color=self.color,
            radius=self.radius,
        )
