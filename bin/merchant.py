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
        self.image = pygame.transform.smoothscale(pygame.image.load("assets/merchantAnimations/blue/blueMerchant1.png").convert_alpha(), (48, 64))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.type = type

        ## animation variables ##
        self.animation_frame = "blueMerchant1.png"
        self.current_iteration = 0
        self.frame = 0
        self.animation_folder = filename
        self.animation_rate = 2

    def update(self):
        """
        Used for updating the animation frame for the merchant
        args: None
        return: none
        """
        self.current_iteration = bin.functions.currentIterationChecker(self.current_iteration, self.animation_folder)
        (self.animation_frame, self.current_iteration, self.frame) = bin.functions.animate(self.animation_folder, self.animation_rate, self.current_iteration, self.frame, self.animation_frame)
        self.image = pygame.transform.smoothscale(pygame.image.load(self.animation_folder + "/" + self.animation_frame).convert_alpha(), (100, 100))
        temporary = self.image.get_rect()
        temporary.x = self.rect.x
        temporary.y = self.rect.y
        self.rect = temporary
