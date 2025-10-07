import pygame

class SettingsMenu:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        self.fullscreen = False
        self.resolutions = [(800,600),(1280,720),(1920,1080)]
        self.current_res_index = 0

        self.options = ["Разрешение","Полноэкран"]
        self.selected = 0

        self.font_big = pygame.font.Font(None, 72)
        self.font_small = pygame.font.Font(None, 48)

    def draw(self):
        self.window.fill((30,30,60))
        width, height = self.window.get_size()

        title = self.font_big.render("Настройки Игры", True, (255,200,50))
        self.window.blit(title,(width//2 - title.get_width()//2, 100))

        res_text = f"Разрешение: {self.resolutions[self.current_res_index][0]}x{self.resolutions[self.current_res_index][1]}"
        color = (255,255,0) if self.selected==0 else (180,180,180)
        self.window.blit(self.font_small.render(res_text,True,color),
                         (width//2 - self.font_small.size(res_text)[0]//2, 300))

        fs_text = f"Полноэкран: {'Да' if self.fullscreen else 'Нет'}"
        color = (255,255,0) if self.selected==1 else (180,180,180)
        self.window.blit(self.font_small.render(fs_text,True,color),
                         (width//2 - self.font_small.size(fs_text)[0]//2, 400))

        instr_text = "←/→ менять, ↑/↓ переключать, Enter - выход"
        instr = self.font_small.render(instr_text, True, (200, 200, 200))
        self.window.blit(instr, (width//2 - self.font_small.size(instr_text)[0]//2, 500))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    elif event.key == pygame.K_LEFT:
                        if self.selected == 0:
                            self.current_res_index = (self.current_res_index - 1) % len(self.resolutions)
                        elif self.selected == 1:
                            self.fullscreen = not self.fullscreen
                    elif event.key == pygame.K_RIGHT:
                        if self.selected == 0:
                            self.current_res_index = (self.current_res_index + 1) % len(self.resolutions)
                        elif self.selected == 1:
                            self.fullscreen = not self.fullscreen
                    elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        return "menu"

                    # Применяем настройки сразу
                    width, height = self.resolutions[self.current_res_index]
                    flags = pygame.FULLSCREEN if self.fullscreen else 0
                    pygame.display.set_mode((width,height), flags)

            self.draw()
            self.clock.tick(60)
