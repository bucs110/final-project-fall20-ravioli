import pygame
import bin.controller

class Score(pygame.sprite.Sprite):
    def __init__ (self, highScore):
        """
        creates JSON high score data permanence feature
        args: highScore --> (int) high score
        return: none
        """
        pygame.sprite.Sprite.__init__(self)
        self.highScore = highScore

    def changeScore(self, newScore):
        """
        changes score if new score is higher than current high score
        """
        #check if new high score or not and update that object here
        #pass in new score from game and compare with high score- keep track of new score in controller separatley and pass it in here
        if self.newScore > self.highScore:
            self.highScore = self.newScore
            

