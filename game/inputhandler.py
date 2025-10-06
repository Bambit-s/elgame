import pygame

class InputHandler:
    """Обработчик ввода: поддержка одноразового и удерживаемого ввода"""

    def __init__(self):
        self.keys = pygame.key.get_pressed()
        self.prev_keys = self.keys

    def update(self):
        self.prev_keys = self.keys
        self.keys = pygame.key.get_pressed()

    # --- одноразовое нажатие ---
    def pressed(self, key):
        return self.keys[key] and not self.prev_keys[key]

    # --- удержание (для плавного движения) ---
    def held(self, key):
        return self.keys[key]

    # --- навигация в меню (одноразово) ---
    def menu_up(self):
        return self.pressed(pygame.K_UP) or self.pressed(pygame.K_w)

    def menu_down(self):
        return self.pressed(pygame.K_DOWN) or self.pressed(pygame.K_s)

    def action(self):
        return self.pressed(pygame.K_RETURN) or self.pressed(pygame.K_SPACE)

    def escape(self):
        return self.pressed(pygame.K_ESCAPE)

    # --- движение персонажа (удержание) ---
    def up(self):
        return self.held(pygame.K_UP) or self.held(pygame.K_w)

    def down(self):
        return self.held(pygame.K_DOWN) or self.held(pygame.K_s)

    def left(self):
        return self.held(pygame.K_LEFT) or self.held(pygame.K_a)

    def right(self):
        return self.held(pygame.K_RIGHT) or self.held(pygame.K_d)
