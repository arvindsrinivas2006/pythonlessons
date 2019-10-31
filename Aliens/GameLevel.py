import pygame
from pygame.locals import *

class GameLevel(pygame.sprite.Sprite):
    level = 1  # player level

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.font = pygame.font.Font(None, 48)
        self.font.set_italic(1)
        self.color = Color('orange')
        self.last_level = -1
        self.update()
        self.rect = self.image.get_rect().move(450, 5)

    def update(self):
        if self.level != self.last_level:
            self.last_level = self.level
            msg = "Level: %d" % self.level
            self.image = self.font.render(msg, 0, self.color)

