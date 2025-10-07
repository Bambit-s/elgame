import pygame
from settings import WIDTH, HEIGHT, MAP_WIDTH, MAP_HEIGHT
from player import Player
from camera import Camera
from map import GameMap
from menu import Menu
from inputhandler import InputHandler
from clocktimer import ClockTimer
from pausemenu import PauseMenu  # добавьте импорт

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
        player = Player(400, 300)
        sprite_player = pygame.sprite.Group(player)
        camera = Camera(MAP_WIDTH, MAP_HEIGHT)

        running = True
        paused = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.input_handler.update()
            if not paused and self.input_handler.escape():
                paused = True
                self.time.pause()  # пауза таймера
                pause_result = self.pause_menu.run()  # исправлено: вызываем метод run()
                if pause_result == "resume":
                    paused = False
                    self.time.resume()  # возобновление таймера
                elif pause_result == "menu" or pause_result == "quit":
                    return  # выход в главное меню

            if paused:
                continue  # не обновляем игру, только меню паузы

            # движение игрока через InputHandler
            player.update(self.input_handler)
            camera.update(player.rect)

            # отрисовка
            game_map.draw(self.window, camera)
            for sprite in sprite_player:
                self.window.blit(sprite.image, camera.apply(sprite.rect))
            self.time.draw(self.window)
            pygame.display.flip()
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.input_handler.update()
            if not paused and self.input_handler.escape():
                paused = True
                self.time.pause()  # пауза таймера
                pause_result = self.pause_menu.run()  # исправлено: вызываем метод run()
                if pause_result == "resume":
                    paused = False
                    self.time.resume()  # возобновление таймера
                elif pause_result == "menu" or pause_result == "quit":
                    return  # выход в главное меню

            if paused:
                continue  # не обновляем игру, только меню паузы

            # движение игрока через InputHandler
            player.update(self.input_handler)
            camera.update(player.rect)

            # отрисовка
            game_map.draw(self.window, camera)
            for sprite in sprite_player:
                self.window.blit(sprite.image, camera.apply(sprite.rect))
            self.time.draw(self.window)
            pygame.display.flip()
            self.clock.tick(60)

