import pygame
import bin.functions

class Character(pygame.sprite.Sprite):
    def __init__(self, position, filename, boundaries):
        """
        initialzes the user's Character
        Args:
        position --> (touple) the character's (x,y) coordinates
        filename --> (str) the name of the file of the character's image
        boundaries --> (touple) the limits to where the character can move
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

        (self.upper_boundry, self.lower_boundry, self.left_boundry, self.right_boundry) = boundaries
        self.direction = "right"
        self.STATE = "movement"


        self.hit_ratio = 1.0
        self.health = 100
        self.cooldown_timer = 1500 ## ~5 seconds ##


    def moveUp(self):
        """
        Moves the character upwards
        Args: none
        Return:None
        """
        if self.rect.y > self.upper_boundry:
            self.rect.y -= 1
        self.direction = "up"


    def moveDown(self):
        """
        Moves the character upwards
        Args: none
        Return: None
        """
        if self.rect.y < self.lower_boundry:
            self.rect.y += 1
        self.direction = "down"


    def moveRight(self):
        """
        Moves the character upwards
        Args: none
        Return: None
        """

        if self.rect.x < self.right_boundry:
            self.rect.x += 1
        self.direction = "right"


    def moveLeft(self):
        """
        Moves the character upwards
        Args: none
        Return:None
        """
        if self.rect.x > self.left_boundry:
            self.rect.x -= 1
        self.direction = "left"

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


    def knockBack(self):
        """
        Knocks back the user after being hit
        Args: None
        Return: None
        """
        bounce_back = 75
        self.direction = bin.functions.makeOppositeDirections(self.direction)
        if self.direction == "up":
            self.rect.y -= bounce_back
            if self.rect.y < self.upper_boundry:
                self.rect.y = self.upper_boundry
        elif self.direction == "down":
            self.rect.y += bounce_back
            if self.rect.y > self.lower_boundry:
                self.rect.y = self.lower_boundry
        elif self.direction == "right":
            self.rect.x += bounce_back
            if self.rect.x > self.right_boundry:
                self.rect.x = self.right_boundry
        elif self.direction == "left":
            self.rect.x -= bounce_back
            if self.rect.x < self.left_boundry:
                self.rect.x = self.left_boundry

    def givePosition(self):
        """
        get the current position and direction of the character
        args: None
        Return: (touple) the characters position and direction
        """
        return (self.rect.x, self.rect.y, self.direction)

    def attackMode(self):
        """
        changes the state of the character to attack
        Args: none
        Return: None
        """
        self.state = "attack"

    def update(self):
        """
        Updates the model for a single frame
        Args: None
        Return: None
        """
        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1
