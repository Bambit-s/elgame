import pygame
from settings import MAP_WIDTH, MAP_HEIGHT
from inputhandler import InputHandler
from bullet import Bullet  
from enemy import Enemy  

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill((200, 50, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 3
        self.bullets = pygame.sprite.Group()
        self.shoot_delay = 300
        self.last_shot = pygame.time.get_ticks()

    def update(self, input_handler: InputHandler, enemies=None):
        if input_handler.up():
            self.rect.y -= self.speed
        if input_handler.down():
            self.rect.y += self.speed
        if input_handler.left():
            self.rect.x -= self.speed
        if input_handler.right():
            self.rect.x += self.speed

        self.rect.x = max(0, min(self.rect.x, MAP_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, MAP_HEIGHT - self.rect.height))

        now = pygame.time.get_ticks()
        for bullet in self.bullets:
            if bullet.distance_from_spawn() > 500:
                bullet.kill()
            # обновляем направление к ближайшему врагу
            if enemies and len(enemies) > 0:
                nearest = None
                nearest_dist = None
                for e in enemies:
                    dist = ((e.rect.centerx - bullet.rect.centerx) ** 2 + (e.rect.centery - bullet.rect.centery) ** 2) ** 0.5
                    if nearest is None or dist < nearest_dist:
                        nearest = e
                        nearest_dist = dist
                if nearest:
                    vec_x = nearest.rect.centerx - bullet.rect.centerx
                    vec_y = nearest.rect.centery - bullet.rect.centery
                    norm = (vec_x ** 2 + vec_y ** 2) ** 0.5
                    if norm > 0:
                        bullet.dx = vec_x / norm
                        bullet.dy = vec_y / norm

        if len(self.bullets) == 0 and now - self.last_shot > self.shoot_delay:
            self.auto_shoot(enemies)
            self.last_shot = now

        self.bullets.update()

    def auto_shoot(self, enemies):
        dx, dy = 0, -1
        min_dist = 500
        target = None
        if enemies and len(enemies) > 0:
            nearest = None
            nearest_dist = None
            for e in enemies:
                dist = ((e.rect.centerx - self.rect.centerx) ** 2 + (e.rect.centery - self.rect.centery) ** 2) ** 0.5
                if dist <= min_dist and (nearest is None or dist < nearest_dist):
                    nearest = e
                    nearest_dist = dist
            if nearest:
                vec_x = nearest.rect.centerx - self.rect.centerx
                vec_y = nearest.rect.centery - self.rect.centery
                norm = (vec_x ** 2 + vec_y ** 2) ** 0.5
                if norm > 0:
                    dx = vec_x / norm
                    dy = vec_y / norm
                else:
                    dx, dy = 0, -1
            else:
                return
        self.bullets.add(Bullet(self.rect.centerx, self.rect.centery, dx, dy))

    def draw_bullets(self, surface, camera):
        for bullet in self.bullets:
            surface.blit(bullet.image, camera.apply(bullet.rect))
