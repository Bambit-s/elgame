import pygame
from settings import WIDTH, HEIGHT, MAP_WIDTH, MAP_HEIGHT
from player import Player
from camera import Camera
from map import GameMap
from menu import Menu
from inputhandler import InputHandler

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("RUSSIANS vs PYTHONS")
        self.clock = pygame.time.Clock()

        self.menu = Menu(self.window)
        self.input_handler = InputHandler()

    def run(self):
        while True:
            action = self.menu.run()
            if action == "play":
                self.play()
            elif action == "quit":
                pygame.quit()
                break

    def play(self):
        game_map = GameMap()
        player = Player(400, 300)
        sprite_player = pygame.sprite.Group(player)
        camera = Camera(MAP_WIDTH, MAP_HEIGHT)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # обновляем InputHandler
            self.input_handler.update()

            # выход в меню
            if self.input_handler.escape():
                running = False

            # движение игрока через InputHandler
            player.update(self.input_handler)
            camera.update(player.rect)

            # отрисовка
            game_map.draw(self.window, camera)
            for sprite in sprite_player:
                self.window.blit(sprite.image, camera.apply(sprite.rect))

            pygame.display.flip()
            self.clock.tick(60)

