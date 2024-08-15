import math
from settings import *
import pygame as pg
class Cube:
    def __init__(self, surface, edges, vertices, color, camera_pos:tuple, angle_x, angle_y, distance:int) -> None:
        self.camera_x, self.camera_y, self.camera_z = camera_pos
        self.distance = distance
        self.angle_x = angle_x
        self.angle_y = angle_y
        self.color = color
        self.edges = edges
        self.vertices = vertices
        self.surface = surface
    def project_3d_to_2d(self, point, camera_x, camera_y, camera_z, angle_x, angle_y, distance):
        x, y, z = point

        # Apply camera position (translation)
        x -= camera_x
        y -= camera_y
        z -= camera_z

        # Rotate around the Y axis
        temp_x = x * math.cos(angle_y) - z * math.sin(angle_y)
        temp_z = x * math.sin(angle_y) + z * math.cos(angle_y)
        x, z = temp_x, temp_z

        # Rotate around the X axis
        temp_y = y * math.cos(angle_x) - z * math.sin(angle_x)
        temp_z = y * math.sin(angle_x) + z * math.cos(angle_x)
        y, z = temp_y, temp_z

        # Projection transformation
        factor = distance / (distance + z)
        x_proj = int(WIDTH / 2 + x * factor * 200)
        y_proj = int(HEIGHT / 2 - y * factor * 200)

        return (x_proj, y_proj)
    def projected_points(self):
        projected_points = [
            self.project_3d_to_2d(vertex, self.camera_x, self.camera_y, self.camera_z, self.angle_x, self.angle_y, 3)
            for vertex in self.vertices
        ]

        return projected_points
    def draw(self):
        projected_points = self.projected_points()
        for edge in self.edges:
            p1, p2 = projected_points[edge[0]], projected_points[edge[1]]
            pg.draw.line(self.surface, self.color, p1, p2, 2)