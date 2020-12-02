import pygame

class Score():
    def __init__ (self, highScore):
        """
        initiaizlizes JSON high score data permanence feature
        args: highScore --> (int) high score
        return: none
        """
        self.bestTime = highScore


    def changeScore(self, newScore):
        """
        changes score if new score is higher than current high score
        args: newScore --> (int) the score that the current player earned in the game
        return: none
        """
        if newScore < self.bestTime:
            self.bestTime = newScore
