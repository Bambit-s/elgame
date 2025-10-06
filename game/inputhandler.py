import pygame

class InputHandler:
    """Обработчик ввода с поддержкой одноразового нажатия"""

    def __init__(self):
        self.keys = pygame.key.get_pressed()
        self.prev_keys = self.keys

    def update(self):
        self.prev_keys = self.keys
        self.keys = pygame.key.get_pressed()

    def pressed(self, key):
        return self.keys[key] and not self.prev_keys[key]

    def up(self):
        return self.pressed(pygame.K_UP) or self.pressed(pygame.K_w)

    def down(self):
        return self.pressed(pygame.K_DOWN) or self.pressed(pygame.K_s)

    def left(self):
        return self.pressed(pygame.K_LEFT) or self.pressed(pygame.K_a)

    def right(self):
        return self.pressed(pygame.K_RIGHT) or self.pressed(pygame.K_d)

    def action(self):
        return self.pressed(pygame.K_RETURN) or self.pressed(pygame.K_SPACE)

    def escape(self):
        return self.pressed(pygame.K_ESCAPE)
