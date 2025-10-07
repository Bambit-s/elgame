import pygame

class ClockTimer:
    def __init__(self, font=None, color=(255,255,255)):
        self.start_ticks = pygame.time.get_ticks()
        self.paused = False
        self.pause_ticks = 0
        self.font = font or pygame.font.Font(None, 48)
        self.color = color

    def reset(self):
        self.start_ticks = pygame.time.get_ticks()
        self.paused = False
        self.pause_ticks = 0

    def pause(self):
        if not self.paused:
            self.paused = True
            self.pause_ticks = pygame.time.get_ticks()

    def resume(self):
        if self.paused:
            paused_duration = pygame.time.get_ticks() - self.pause_ticks
            self.start_ticks += paused_duration
            self.paused = False

    def get_seconds(self):
        if self.paused:
            elapsed = self.pause_ticks - self.start_ticks
        else:
            elapsed = pygame.time.get_ticks() - self.start_ticks
        return elapsed // 1000

    def draw(self, surface, pos=(20, 20)):
        seconds = self.get_seconds()
        minutes = seconds // 60
        sec = seconds % 60
        time_str = f"{minutes:02}:{sec:02}"
        img = self.font.render(time_str, True, self.color)
        surface.blit(img, pos)