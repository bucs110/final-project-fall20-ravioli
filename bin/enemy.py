import pygame
import random
import bin.functions

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position, filename):
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

    def update(self):
        """
        Updates the model for a single frame
        Args: None
        Return:
        """
        speed = 100
        self.direction = bin.functions.randomDirection(self.count, self.direction)
        if self.direction == "up" and self.rect.y > 100:
            self.rect.y -= 1
            self.count += 1
            if self.count == speed:
                self.count = 0
        if self.direction == "down" and self.rect.y < 700:
            self.rect.y += 1
            self.count += 1
            if self.count == speed:
                self.count = 0
        if self.direction == "right" and self.rect.x < 1400:
            self.rect.x += 1
            self.count += 1
            if self.count == speed:
                self.count = 0
        if self.direction == "left" and self.rect.x > 100:
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
