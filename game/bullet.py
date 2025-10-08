import pygame
from settings import MAP_WIDTH, MAP_HEIGHT

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.pos_x = float(x)
        self.pos_y = float(y)
        self.dx = dx
        self.dy = dy
        self.speed = 5
        self.spawn_pos = (x, y)

    def update(self):
        self.pos_x += self.dx * self.speed
        self.pos_y += self.dy * self.speed
        self.rect.centerx = int(self.pos_x)
        self.rect.centery = int(self.pos_y)
        if (self.rect.right < 0 or self.rect.left > MAP_WIDTH or
            self.rect.bottom < 0 or self.rect.top > MAP_HEIGHT):
            self.kill()

    def distance_from_spawn(self):
        dx = self.pos_x - self.spawn_pos[0]
        dy = self.pos_y - self.spawn_pos[1]
        return (dx**2 + dy**2) ** 0.5
