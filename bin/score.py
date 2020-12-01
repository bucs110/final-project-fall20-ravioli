import pygame
import bin.controller

class Score():
    def __init__ (self, highScore):
        """
        creates JSON high score data permanence feature
        args: highScore --> (int) high score
        return: none
        """
        self.bestTime = highScore


    def changeScore(self, newScore):
        """
        changes score if new score is higher than current high score
        args: newScore --> (int) the score that the current player got on the game
        return: none
        """
        #check if new high score or not and update that object here
        #pass in new score from game and compare with high score- keep track of new score in controller separatley and pass it in here
        if newScore < self.bestTime:
            self.bestTime = newScore
