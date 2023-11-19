from typing import Optional
from dataclasses import dataclass
from pygame import Color, Surface
from Circle import Circle
from Utils.VectorMath import Vector, Point

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
        for i in range(0, len(self.labels)):
            self.labels[i].point = self.points[i].point - Point(0, 10)

    def add_point(self, point: Point):
        # Point
        self.points.append(Circle(point, POINT_RADIUS, Color(0, 0, 255)))

        # Label
        self.labels.append(Circle(point, LABEL_RADIUS, Color(0, 255, 0)))

        self._calc_label_positions()

    def render(self, surface: Surface):
        for i in range(0, len(self.points)):
            self.points[i].render(surface)
            self.labels[i].render(surface)
