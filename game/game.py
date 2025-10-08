import pygame
from settings import WIDTH, HEIGHT, MAP_WIDTH, MAP_HEIGHT
from player import Player
from camera import Camera
from map import GameMap
from menu import Menu
from inputhandler import InputHandler
from clocktimer import ClockTimer
from pausemenu import PauseMenu  # добавьте импорт
from enemy import Enemy  # убедитесь, что импорт есть
import random

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("RUSSIANS vs PYTHONS")
        self.clock = pygame.time.Clock()

        self.menu = Menu(self.window)
        self.input_handler = InputHandler()
        self.time = ClockTimer()
        self.pause_menu = PauseMenu(self.window)  # создайте экземпляр

    def run(self):
        while True:
            action = self.menu.run()
            if action == "play":
                self.play()
            elif action == "quit":
                pygame.quit()
                break

    def play(self):
        self.time.reset()  # сброс таймера при старте игры
        game_map = GameMap()
        player = Player(1000, 1000)
        sprite_player = pygame.sprite.Group(player)
        camera = Camera(MAP_WIDTH, MAP_HEIGHT)

        import math
        import time

        def spawn_enemy_near_player():
            while True:
                angle = random.uniform(0, 2 * math.pi)
                dist = random.randint(800, 1200)  # диапазон: не ближе 800, не дальше 1200
                x = int(player.rect.centerx + dist * math.cos(angle))
                y = int(player.rect.centery + dist * math.sin(angle))
                # ограничение по карте
                x = max(32, min(x, MAP_WIDTH - 32))
                y = max(32, min(y, MAP_HEIGHT - 32))
                # проверяем дистанцию
                actual_dist = ((x - player.rect.centerx) ** 2 + (y - player.rect.centery) ** 2) ** 0.5
                if actual_dist >= 800:
                    return Enemy(x, y)

        enemies = pygame.sprite.Group()  # пустая группа

        running = True
        paused = False
        first_spawn_delay = 5  # секунд
        spawn_time = pygame.time.get_ticks()
        first_spawned = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.input_handler.update()
            if not paused and self.input_handler.escape():
                paused = True
                self.time.pause()
                pause_result = self.pause_menu.run()
                if pause_result == "resume":
                    paused = False
                    self.time.resume()
                elif pause_result == "menu" or pause_result == "quit":
                    return

            if paused:
                continue

            player.update(self.input_handler, enemies)
            camera.update(player.rect)
            enemies.update(player)

            hits = pygame.sprite.groupcollide(enemies, player.bullets, False, True)
            for enemy in hits:
                enemy.hit()

            # --- задержка перед первой генерацией врагов ---
            elapsed_sec = (pygame.time.get_ticks() - spawn_time) // 1000
            if not first_spawned and elapsed_sec >= first_spawn_delay:
                for _ in range(10):
                    enemies.add(spawn_enemy_near_player())
                first_spawned = True

            # --- поддержание 10 врагов ---
            if first_spawned:
                while len(enemies) < 10:
                    enemies.add(spawn_enemy_near_player())

            game_map.draw(self.window, camera)
            for sprite in sprite_player:
                self.window.blit(sprite.image, camera.apply(sprite.rect))
            for enemy in enemies:
                self.window.blit(enemy.image, camera.apply(enemy.rect))
            player.draw_bullets(self.window, camera)
            self.time.draw(self.window)
            pygame.display.flip()
            self.clock.tick(60)

