import pygame
from settings import MAP_WIDTH, MAP_HEIGHT

class GameMap:
    def __init__(self):
        self.surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))
        self.surface.fill((30, 30, 50))
        for i in range(300):
            pygame.draw.circle(
                self.surface,
                (0, 150, 0),
                (i * 40 % MAP_WIDTH, (i * 60) % MAP_HEIGHT),
                10
            )

    def draw(self, window, camera):
        window.blit(self.surface, (-camera.camera_x, -camera.camera_y))
