import pygame


class BubbleShieldBox(pygame.sprite.Sprite):
    """
        This is a defensive power up!
    """
    is_active = False
    
    images = []
    animation_cycle = 10
    def __init__(self, screen_rectangle):
        """
        this is the constructor! Gets called when class is
        initialized
        """
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.frame = 0
        self.image = self.images[0]

        self.image_size = self.image.get_size()
        self.image_size = (
            int(self.image_size[0]*.6), int(self.image_size[1]*.6)
        )
        self.image = pygame.transform.scale(
            self.image, self.image_size)
        
        

        # create hitbox and position the bubble shield around tank
        self.rect = self.image.get_rect(bottom=(screen_rectangle.bottom -10))
    
    def update(self):
        if(self.is_active is True):
            self.frame = self.frame + 1
            
            self.image = self.images[self.frame//self.animation_cycle % 2]
        else:
            # hiding the bubble shield box
            self.frame = 0
            self.image = self.images[self.frame]


        
        