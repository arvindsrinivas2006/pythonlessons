import pygame
import random

class SpaceMonster(pygame.sprite.Sprite):
    # class level variables
    health = 100

    # this is the animation of the alien on the screen
    images = []

    def __init__(self, screen_rectangle):
        """
        this is the constructor! Gets called when class is
        initialized
        """
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        # size the space monster game object by using the first
        # image in the collection
        self.image = self.images[0]

        self.image_size = self.image.get_size()

        # image is too big. scale down
        self.image_size = (
            int(self.image_size[0]*.7), int(self.image_size[1]*.7)
        )
        self.image = pygame.transform.scale(
            self.image, self.image_size)

        # create hitbox and position the space monster
        self.rect = self.image.get_rect(midtop=screen_rectangle.
        midtop)

        self.x_velocity = 10

    def update(self):
        if(self.health < 1):
            self.kill()
        else:
            if(self.health < 50 and self.health > 19):
                self.image = self.images[1]
            else:
                self.image = self.images[0]

            # let's shake the space monster left and right!!
            self.x_velocity = random.randint(-10, 10)

            self.rect.move_ip(self.x_velocity, 0)
            
        
        

