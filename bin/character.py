import pygame
import bin.functions

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

        self.direction = "right"

        self.health = 100
        self.cooldown_timer = 1500 ## ~5 seconds ##


    def moveUp(self, upper_boundry):
        """
        Moves the character upwards
        Args: upper_boundry --> (int) the upper limit for the character to move
        Return:None
        """
        if self.rect.y > upper_boundry:
            self.rect.y -= 1
        self.direction = "up"


    def moveDown(self, lower_boundry):
        """
        Moves the character upwards
        Args: lower_boundry --> (int) the lower limit for the character to move
        Return: None
        """
        if self.rect.y < lower_boundry:
            self.rect.y += 1
        self.direction = "down"


    def moveRight(self, right_boundry):
        """
        Moves the character upwards
        Args: right_boundry --> (int) the rightward limit for the character to move
        Return: None
        """

        if self.rect.x < right_boundry:
            self.rect.x += 1
        self.direction = "right"


    def moveLeft(self, left_boundry):
        """
        Moves the character upwards
        Args: left_boundry --> (int) the leftward limit for the character to move
        Return:None
        """
        if self.rect.x > left_boundry:
            self.rect.x -= 1
        self.direction = "left"


    def draw(self, screen):
        """
        Used to draw and update the enemy class
        Args: None
        Return: None
        """
        screen.blit(self.character.image, (self.character.rect.x, self.character.rect.y))


    def gotHit(self):
        """
        used to reduce the health of the character when it gets hit
        Args: None
        Return: (str) alive or dead
        """
        if self.cooldown_timer == 0:
            self.health -= 10
            self.cooldown_timer = 900 ## resets cooldown_timer ~3 seconds ##
        print(str(self.health) + " character")
        if self.health == 0:
            return "dead"
        else:
            return "alive"


    def knockBack(self, upper_boundry, lower_boundry, right_boundry, left_boundry ):
        """
        Knocks back the user after being hit
        Args:
        upper_boundry --> (int) the upper limit for the character to move
        lower_boundry --> (int) the lower limit for the character to move
        right_boundry --> (int) the rightward limit for the character to move
        left_boundry --> (int) the leftward limit for the character to move
        Return: None
        """
        bounce_back = 75
        self.direction = bin.functions.makeOppositeDirections(self.direction)
        if self.direction == "up":
            self.rect.y -= bounce_back
            if self.rect.y < upper_boundry:
                self.rect.y = upper_boundry
        elif self.direction == "down":
            self.rect.y += bounce_back
            if self.rect.y > lower_boundry:
                self.rect.y = lower_boundry
        elif self.direction == "right":
            self.rect.x += bounce_back
            if self.rect.x > right_boundry:
                self.rect.x = right_boundry
        elif self.direction == "left":
            self.rect.x -= bounce_back
            if self.rect.x < left_boundry:
                self.rect.x = left_boundry

    def givePosition(self):
        """
        get the current position and direction of the character
        args: None
        Return: (touple) the characters position and direction
        """
        return (self.rect.x, self.rect.y, self.direction)

    def update(self):
        """
        Updates the model for a single frame
        Args: None
        Return: None
        """
        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1
