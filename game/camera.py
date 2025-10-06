import pygame
from settings import WIDTH, HEIGHT

class Camera:
    def __init__(self, map_width, map_height):
        self.camera_x = 0
        self.camera_y = 0
        self.map_width = map_width
        self.map_height = map_height

    def apply(self, rect):
        return rect.move(-self.camera_x, -self.camera_y)

    def update(self, target_rect):
        self.camera_x = target_rect.centerx - WIDTH // 2
        self.camera_y = target_rect.centery - HEIGHT // 2

        # ограничение движения камеры в пределах карты
        self.camera_x = max(0, min(self.camera_x, self.map_width - WIDTH))
        self.camera_y = max(0, min(self.camera_y, self.map_height - HEIGHT))
