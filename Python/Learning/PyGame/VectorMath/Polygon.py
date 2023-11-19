from typing import Optional
from dataclasses import dataclass
from pygame import Color, Surface
from Circle import Circle
from Line import Line
from Utils.VectorMath import Vector, Point
import pygame

POINT_RADIUS = 10
LABEL_RADIUS = 5


@dataclass
class Polygon:
    points: Optional[Circle] = None
    labels: Optional[Circle] = None

    def __init__(self):
        self.points = []
        self.labels = []

    def _calc_label_positions(self):
        pl = len(self.points)
        for i in range(pl-1, -1, -1):
            if pl == 1:
                self.labels[i].point = self.points[i].point - Point(0, 10)
            elif pl > 1 and i > 0 :
                self.labels[i].point = (self.points[i-1].point + Vector(self.points[i-1].point, self.points[i].point)) * 1.1

    def add_point(self, point: Point):
        # Point
        self.points.append(Circle(point, POINT_RADIUS, Color(0, 0, 255)))

        # Label
        self.labels.append(Circle(point, LABEL_RADIUS, Color(0, 255, 0)))

        self._calc_label_positions()

    def render(self, surface: Surface):
        if len(self.points) > 1:
            pygame.draw.lines(surface=surface, color=Color(255, 255, 255), closed=False, points=[(point.point.x, point.point.y) for point in self.points])
            
        for i in range(0, len(self.points)):
            self.points[i].render(surface)
            self.labels[i].render(surface)
