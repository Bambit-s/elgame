import pygame
from settings import PLAYER_SPEED, MAP_WIDTH, MAP_HEIGHT
from inputhandler import InputHandler

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill((200, 50, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = PLAYER_SPEED

    def update(self, input_handler: InputHandler):
        if input_handler.up():
            self.rect.y -= self.speed
        if input_handler.down():
            self.rect.y += self.speed
        if input_handler.left():
            self.rect.x -= self.speed
        if input_handler.right():
            self.rect.x += self.speed

        # ограничение игрока в пределах карты
        self.rect.x = max(0, min(self.rect.x, MAP_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, MAP_HEIGHT - self.rect.height))
