import pygame
from Utils.VectorMath import Point


class Line:
    def __init__(self, start: Point, end: Point, color: pygame.Color):
        self.start = start
        self.end = end
        self.color = color