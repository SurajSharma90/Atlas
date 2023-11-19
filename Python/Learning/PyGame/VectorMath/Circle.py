import pygame
from Utils.VectorMath import Point


class Circle:
    def __init__(self, point: Point, radius: float, color: pygame.Color):
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
