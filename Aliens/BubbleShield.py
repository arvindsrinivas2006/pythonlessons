import pygame


class BubbleShield(pygame.sprite.Sprite):
    """
        This is a defensive power up!
    """
    is_active = False
    
    images = []
    
    def __init__(self, tank):
        """
        this is the constructor! Gets called when class is
        initialized
        """
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.image = self.images[0]

        # create hitbox and position the bubble shield around tank
        self.rect = self.image.get_rect(center=(tank.rect.center))
    
    def visibility(self, is_visible):
        
        """
        load image of bubble shield
        """
        if(is_visible is True):
            # show bubble shield
            self.image = self.images[1]
        
            self.is_active = True
        else:
        # show a TRANSPARENT bubble shield-- "hide"
            self.image = self.images[0]
            
            self.is_active = False
            
    def move(self, tank):
        # update hitbox and position the bubble shield around tank
        self.rect = self.image.get_rect(center=(tank.rect.center))
       