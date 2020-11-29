import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, position, filename, use, size):
        """
        initialzes a button object
        args:
        position --> (touple) the buttons location on the screen
        filename --> (str) the file for the png of the button
        use --> (str) a string for what the button is used for
        size --> (touple) the size for the button
        """
        self.size = size
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.smoothscale(pygame.image.load(filename).convert_alpha(), self.size)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.use = use

    def toggle(self, filename):
        """
        toggles the button to show it has been clicked
        args: filename --> (str) the name of the file for the toggle png
        return: none
        """
        self.image = pygame.transform.smoothscale(pygame.image.load(filename).convert_alpha(), self.size)
        temporary = self.image.get_rect()
        temporary.x = self.rect.x
        temporary.y = self.rect.y
        self.rect = temporary
