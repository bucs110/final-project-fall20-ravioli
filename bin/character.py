import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, position, filename):
        """
        initialzes the user's Character
        Args:
        position --> (touple) the character's (x,y) coordinates
        filename --> (str) the name of the file of the character's image
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        ###self.direction = 'left' ##this might be different

    def moveUp(self):
        """
        Moves the character upwards
        Args: None
        Return:None
        """
        if self.rect.y > 100:
            self.rect.y -= 1

    def moveDown(self):
        """
        Moves the character upwards
        Args: None
        Return:None
        """
        if self.rect.y < 700:
            self.rect.y += 1

    def moveRight(self):
        """
        Moves the character upwards
        Args: None
        Return:None
        """

        if self.rect.x < 1400:
            self.rect.x += 1

    def moveLeft(self):
        """
        Moves the character upwards
        Args: None
        Return:None
        """
        if self.rect.x > 100:
            self.rect.x -= 1

    def update(self):
        """
        Updates the model for a single frame
        Args: None
        Return:
        """
