import pygame
import bin.functions

class Melee(pygame.sprite.Sprite):
    def __init__(self, sword_length, filename):
        """
        initialzes melee weapons
        Args:
        sword_length --> (int) pixel length of the sword
        filename --> (str) the name of the file of the character's image
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()

        ##set these up for calculations later on##
        self.character_pixel_height = 43
        self.character_pixel_width = 50
        self.sword_length = sword_length


    def strike(self, position_and_direction):
        """
        Calculates where the upper left corner of the sword needs to be
        Args:
        position --> (touple) position of the character
        direction --> (str) the direction the character is facing
        """
        (character_x, character_y, direction) = (position_and_direction[0], position_and_direction[1], position_and_direction[2])
        if direction == "up":
            self.rect.y = character_y - self.sword_length
            self.rect.x = character_x + (self.character_pixel_width // 4)
            self.image = pygame.image.load("assets/resizedd_penne_sword_vertical.png")
        elif direction == "down":
            self.rect.y = character_y + self.character_pixel_height
            self.rect.x = character_x + (self.character_pixel_width // 4)
            self.image = pygame.image.load("assets/resizedd_penne_sword_vertical.png")
        elif direction == "right":
            self.rect.x = character_x + (self.character_pixel_width)
            self.rect.y = character_y + (self.character_pixel_height // 4)
            self.image = pygame.image.load("assets/resizedd_penne_sword_horizontal.png")
        elif direction == "left":
            self.rect.x = character_x - self.sword_length
            self.rect.y = character_y + (self.character_pixel_height // 4)
            self.image = pygame.image.load("assets/resizedd_penne_sword_horizontal.png")

    def draw(self, screen):
        """
        Used to draw and update the enemy class
        Args: None
        Return: None
        """
        screen.blit(self.sword.image, (self.sword.rect.x, self.sword.rect.y))

    def update(self):
        """
        updates the sword
        Args: None
        Return: None
        """












        ##give me space thanks##
