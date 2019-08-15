import pygame
from pygame.locals import *
import random

from Explosion import Explosion

class Score(pygame.sprite.Sprite):
    
    score_points = 0 
    
    def __init__(self, alien):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.font = pygame.font.Font(None, 20)
        self.color = Color("white")
        self.font.set_italic(1)
        self.lasts_score = -1
    
        self.update()
        
        self.rect = self.image.get_rect().move(10, 450)
        
    
    def update(self):
        if(self.score_points != self.lasts_score):
            self.lasts_score = self.score_points

            msg = "Score: %d" % self.score_points

            self.image = self.font.render(msg, 0, self.color)
                