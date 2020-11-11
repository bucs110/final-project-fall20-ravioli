import pygame
import random
import bin.functions

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position, health, filename):
        """
        Initializes the enemies for the user
        Args:
        position --> (touple) the enemy's inital coordinates
        filename --> (str) the name of the file for the enemy image
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.count = 0
        self.direction = "up"
        self.health = health
        ## I hate to redefine these but its the easiest way to do this##
        (self.upper_boundry, self.lower_boundry, self.left_boundry, self.right_boundry) = (100, 700, 100, 1400)

    def update(self):
        """
        Updates the model for a single frame
        Args: None
        Return:
        """
        speed = 100
        self.direction = bin.functions.randomDirection(self.count, self.direction)
        self.direction = "none" ##make the enemy stationary for testing purposes##
        if self.direction == "up" and self.rect.y > self.upper_boundry:
            self.rect.y -= 1
            self.count += 1
            if self.count == speed:
                self.count = 0
        if self.direction == "down" and self.rect.y < self.lower_boundry:
            self.rect.y += 1
            self.count += 1
            if self.count == speed:
                self.count = 0
        if self.direction == "right" and self.rect.x < self.right_boundry:
            self.rect.x += 1
            self.count += 1
            if self.count == speed:
                self.count = 0
        if self.direction == "left" and self.rect.x > self.left_boundry:
            self.rect.x -= 1
            self.count += 1
            if self.count == speed:
                self.count = 0
        if self.direction == "none":
            self.count += 1
            if self.count == speed:
                self.count = 0

    def draw(self, screen):
        """
        Used to draw and update the enemy class
        Args: None
        Return: None
        """
        screen.blit(self.enemy.image, (self.enemy.rect.x, self.enemy.rect.y))

    def switchDirection(self):
        """
        Changes the direciton of the enemy
        Args: None
        Return: None
        """
        self.direction = bin.functions.makeOppositeDirections(self.direction)

    def gotHit(self):
        """
        used to reduce the health of the enemy's health when it gets hit
        Args: None
        Return: (str) alive or dead
        """
        ## add knockback ##
        self.health -= 10
        if self.health == 0:
            return "dead"
        else:
            return "alive"

    def knockBack(self, upper_boundry, lower_boundry, right_boundry, left_boundry, position):
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

        self.direction = position[2]

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
        self.direction = "none"
