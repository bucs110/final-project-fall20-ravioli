import pygame
import random
import bin.functions

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type, positionX, positionY, health, filename, boundaries):
        """
        Initializes the enemies for the user
        Args:
        type --> (str) the given type for an enemy ## NOT FULLY IMPLEMENTED YET ##
        positionX --> (int) the enemy's inital X coordinate
        positionY --> (int) the enemy's inital Y coordinate
        filename --> (str) the name of the file for the enemy image
        boundaries --> (touple) the world boundaries for the screen
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = positionX
        self.rect.y = positionY
        self.count = 0
        self.direction = "up"
        self.speed = 3
        self.health = health
        self.reward_money = health
        (self.upper_boundry, self.lower_boundry, self.left_boundry, self.right_boundry) = boundaries


    def update(self):
        """
        Updates the model for a single frame
        Args: None
        Return:
        """
        speed = 75
        self.direction = bin.functions.randomDirection(self.count, self.direction)
        self.direction = "none" ##make the enemy stationary for testing purposes##
        if self.direction == "up" and self.rect.y > self.upper_boundry:
            self.rect.y -= self.speed
            self.count += 1
            if self.count == speed:
                self.count = 0
        if self.direction == "down" and self.rect.y < self.lower_boundry:
            self.rect.y += self.speed
            self.count += 1
            if self.count == speed:
                self.count = 0
        if self.direction == "right" and self.rect.x < self.right_boundry:
            self.rect.x += self.speed
            self.count += 1
            if self.count == speed:
                self.count = 0
        if self.direction == "left" and self.rect.x > self.left_boundry:
            self.rect.x -= self.speed
            self.count += 1
            if self.count == speed:
                self.count = 0
        if self.direction == "none":
            self.count += self.speed
            if self.count == speed:
                self.count = 0

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
        enemy_hit_sound = pygame.mixer.Sound("assets/sounds/enemyHitSound.wav")
        enemy_hit_sound.play()
        if self.health == 0:
            return "dead"


    def knockBack(self, direction):
        """
        Knocks back the user after being hit
        Args:
        direction --> (str) the character's direction
        Return: None
        """
        bounce_back = 75

        self.direction = direction

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
        #self.direction = "none"
