import pygame

class PauseMenu:
    def __init__(self, window):
        self.window = window
        self.font_big = pygame.font.Font(None, 72)
        self.font_small = pygame.font.Font(None, 48)
        self.options = ["Продолжить", "Выйти в меню"]
        self.selected = 0

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_UP, pygame.K_w):
                        self.selected = (self.selected - 1) % len(self.options)
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        self.selected = (self.selected + 1) % len(self.options)
                    elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        if self.options[self.selected] == "Продолжить":
                            return "resume"
                        elif self.options[self.selected] == "Выйти в меню":
                            return "menu"

            self.window.fill((40, 40, 80))
            title = self.font_big.render("Пауза", True, (255, 200, 50))
            self.window.blit(title, (self.window.get_width() // 2 - title.get_width() // 2, 120))
            for i, text in enumerate(self.options):
                color = (255, 255, 255) if i == self.selected else (180, 180, 180)
                render = self.font_small.render(text, True, color)
                self.window.blit(render, (self.window.get_width() // 2 - render.get_width() // 2, 300 + i * 80))
            pygame.display.flip()
            clock.tick(30)
