import pygame
import bin.button


class Merchant(pygame.sprite.Sprite):
    def __init__(self, position, filename, type):
        """
        initilzes the merchant
        Args:
        position --> (touple) the character's (x,y) coordinates
        filename --> (str) the name of the file of the character's image
        type --> (str) the type of merchant
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.smoothscale(pygame.image.load(filename).convert_alpha(), (48, 64))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.type = type


    def exchange(self):
        """
        sets up the exchange between the merchant and the player
        Args: type --> (str) the type of merchant
        Return: (str) upgrade, health, or weapons
        """
        if self.type == "upgrade":
            return "upgrade"
        elif self.type == "health":
            return "health"
        elif self.type == "banker":
            return "banker"
