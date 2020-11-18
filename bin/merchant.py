import pygame


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
        self.image = pygame.transform.smoothscale(pygame.image.load(filename).convert_alpha(), (27,27))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.type = type


    def exchange(self, type):
        """
        sets up the exchange between the merchant and the player
        Args: type --> (str) the type of merchant
        Return: (str) upgrade, health, or weapons
        """
        if type == "upgrade":
            return "upgrade"
        elif type == "health":
            return "health"
        elif type == "banker":
            return "banker"
