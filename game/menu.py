import pygame
from settingmenu import SettingsMenu
from inputhandler import InputHandler

class Menu:
    def __init__(self, window):
        self.window = window
        self.font_big = pygame.font.Font(None, 72)
        self.font_small = pygame.font.Font(None, 48)

        self.options = ["Играть", "Настройка персонажей", "Настройки Игры", "Выход"]
        self.selected = 0

        self.settings_menu = SettingsMenu(self.window)
        self.input_handler = InputHandler()

    def draw(self):
        self.window.fill((20,20,40))
        width, height = self.window.get_size()

        title = self.font_big.render("RUSSIANS vs PYTHONS", True, (255,200,50))
        self.window.blit(title,(width//2 - title.get_width()//2,120))

        for i, text in enumerate(self.options):
            color = (255,255,255) if i==self.selected else (180,180,180)
            render = self.font_small.render(text,True,color)
            self.window.blit(render,(width//2 - render.get_width()//2,300 + i*80))

        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

            # обновляем ввод
            self.input_handler.update()

            # навигация
            if self.input_handler.up():
                self.selected = (self.selected - 1) % len(self.options)
            elif self.input_handler.down():
                self.selected = (self.selected + 1) % len(self.options)
            elif self.input_handler.action():
                choice = self.options[self.selected]
                if choice == "Играть":
                    return "play"
                elif choice == "Выход":
                    return "quit"
                elif choice == "Настройки Игры":
                    self.settings_menu.run()
                elif choice == "Настройка персонажей":
                    pass

            self.draw()
            clock.tick(30)
