import pygame
import settings

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((200, 50, 50))  # красный квадрат, замените на свой спрайт при необходимости
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 2

    def update(self, player):
        # Двигается к игроку
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        dist = max(1, (dx**2 + dy**2) ** 0.5)
        self.rect.x += int(self.speed * dx / dist)
        self.rect.y += int(self.speed * dy / dist)

    def hit(self):
        # Реакция на попадание (например, удаление врага)
        self.kill()