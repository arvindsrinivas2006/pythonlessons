import pygame


class SpaceMonster(pygame.sprite.Sprite):
    # class level variables
    speed = 13

    # this is the animation of the alien on the screen
    images = []

    def__init__(self, screen_rectangle):
        """
        this is the constructor! Gets called when class is
        initialized
        """
        pygame.sprite.Sprite.__init__(self, self.containers)
        

