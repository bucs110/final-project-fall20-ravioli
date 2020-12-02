import pygame
import random
import bin.functions

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type, positionX, positionY, health, speed, boundaries):
        """
        Initializes the enemies and their image, position, fighting stats and abilities, and enemy type
        Args:
        type --> (str) the given type for an enemy ## NOT FULLY IMPLEMENTED YET ##
        positionX --> (int) the enemy's inital X coordinate
        positionY --> (int) the enemy's inital Y coordinate
        speed --> (str) how many pixels the enemy moves with each step
        boundaries --> (touple) the world boundaries for the screen
        Return: none
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.smoothscale(pygame.image.load("assets/enemyAnimations/walkR/enemyWalkR1.png").convert_alpha(), (75,75))
        self.rect = self.image.get_rect()
        self.rect.x = positionX
        self.rect.y = positionY
        self.count = 0

        self.speed = int(speed)
        self.health = health
        self.reward_money = health
        self.damage = 5
        (self.upper_boundry, self.lower_boundry, self.left_boundry, self.right_boundry) = boundaries

        self.characterX = 400
        self.characterY = 400
        self.type = type
        self.direction = "right"


        ## animation variables ##
        self.animation_frame = "enemyWalkL1.png"
        self.current_iteration = 0
        self.frame = 0
        self.animation_folder = "assets/enemyAnimations/walkL"
        self.animation_rate = 2
        self.animation_state = "ACTIVE"

    def update(self):
        """
        Updates the model for a single frame; gives characteristics and abilities (speed and direction of movement)
        to different types of enemies (roamer, tracker, horizontal)
        Args: None
        Return: None
        """
        if self.type == "roamer":
            speed = 75
            self.direction = bin.functions.randomDirection(self.count, self.direction)
            #self.direction = "none" ##make the enemy stationary for testing purposes##
            if self.direction == "up" and self.rect.y > self.upper_boundry:
                self.animation_state = "ACTIVE"
                self.rect.y -= self.speed
                self.count += 1
                if self.rect.y == self.upper_boundry:
                    self.direction = "down"
                if self.count > speed:
                    self.count = 0
            if self.direction == "down" and self.rect.y < self.lower_boundry:
                self.animation_state = "ACTIVE"
                self.rect.y += self.speed
                self.count += 1
                if self.rect.y == self.lower_boundry:
                    self.direction = "up"
                if self.count > speed:
                    self.count = 0
            if self.direction == "right" and self.rect.x < self.right_boundry:
                self.animation_state = "ACTIVE"
                self.animation_folder = "assets/enemyAnimations/walkR"
                self.rect.x += self.speed
                self.count += 1
                if self.rect.x == self.right_boundry:
                    self.direction = "left"
                if self.count > speed:
                    self.count = 0
            if self.direction == "left" and self.rect.x > self.left_boundry:
                self.animation_state = "ACTIVE"
                self.animation_folder = "assets/enemyAnimations/walkL"
                self.rect.x -= self.speed
                self.count += 1
                if self.rect.x == self.left_boundry:
                    self.direction = "right"
                if self.count > speed:
                    self.count = 0
            if self.direction == "none":
                self.animation_state == "INACTIVE"
                self.count += self.speed
                if self.count > speed:
                    self.count = 0

            if self.animation_state == "ACTIVE":
                self.current_iteration = bin.functions.currentIterationChecker(self.current_iteration, self.animation_folder)
                (self.animation_frame, self.current_iteration, self.frame) = bin.functions.animate(self.animation_folder, self.animation_rate, self.current_iteration, self.frame, self.animation_frame)
                self.image = pygame.transform.smoothscale(pygame.image.load(self.animation_folder + "/" + self.animation_frame).convert_alpha(), (75,75))
                temporary = self.image.get_rect()
                temporary.x = self.rect.x
                temporary.y = self.rect.y
                self.rect = temporary

        if self.type == "still":
            pass

        if self.type == "tracker":
            self.follow(self.characterX, self.characterY)

            self.current_iteration = bin.functions.currentIterationChecker(self.current_iteration, self.animation_folder)
            (self.animation_frame, self.current_iteration, self.frame) = bin.functions.animate(self.animation_folder, self.animation_rate, self.current_iteration, self.frame, self.animation_frame)
            self.image = pygame.transform.smoothscale(pygame.image.load(self.animation_folder + "/" + self.animation_frame).convert_alpha(), (75,75))
            temporary = self.image.get_rect()
            temporary.x = self.rect.x
            temporary.y = self.rect.y
            self.rect = temporary

        if self.type == "horizontal":
            if self.direction == "right":
                self.animation_folder = "assets/enemyAnimations/walkR"
                self.rect.x += self.speed
                if self.rect.x > self.right_boundry:
                    self.direction = "left"

            if self.direction == "left":
                self.animation_folder = "assets/enemyAnimations/walkL"
                self.rect.x -= self.speed
                if self.rect.x < self.left_boundry:
                    self.direction = "right"

            self.current_iteration = bin.functions.currentIterationChecker(self.current_iteration, self.animation_folder)
            (self.animation_frame, self.current_iteration, self.frame) = bin.functions.animate(self.animation_folder, self.animation_rate, self.current_iteration, self.frame, self.animation_frame)
            self.image = pygame.transform.smoothscale(pygame.image.load(self.animation_folder + "/" + self.animation_frame).convert_alpha(), (75,75))
            temporary = self.image.get_rect()
            temporary.x = self.rect.x
            temporary.y = self.rect.y
            self.rect = temporary

    def switchDirection(self):
        """
        Changes the direciton of the enemy to the opposite of its current direction
        Args: None
        Return: direction (str) the opposite direction of the current direction
        """
        self.direction = bin.functions.makeOppositeDirections(self.direction)

    def gotHit(self, damage):
        """
        used to reduce the enemy's health when it gets hit and plays sound depending on if enemy is dead or alive
        Args: None
        Return: "dead" --> (str) enemy's health is at or below 0 and the enemy dies
        """
        ## add knockback ##
        self.damage = damage
        self.health -= self.damage
        chosen_sound = random.choice(["assets/sounds/enemyHitSound1.wav", "assets/sounds/enemyHitSound2.wav"])
        enemy_hit_sound = pygame.mixer.Sound(chosen_sound)
        enemy_hit_sound.play()
        if self.health <= 0:
        	death_sound = pygame.mixer.Sound("assets/sounds/enemyDeathSound.wav")
        	death_sound.play()
        	return "dead"

    def knockBack(self, direction):
        """
        Knocks back the enemy 75 pixels in the opposite direction after being hit or until it hits the
        boundary if it would otherwise go out of frame
        Args: direction --> (str) the enemy's direction
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

    def getCharacterCoords(self, coordinates):
        """
        Gets the character's coordinates
        args: coordinates (touple) --> touple containing the character coordinates
        return: none
        """
        self.characterX = coordinates[0]
        self.characterY = coordinates[1]

    def follow(self, characterX, characterY):
        """
        Makes the enemy to follow the character's position
        args:
        characterX --> (int) the character's x coordinate
        characterY --> (int) the character's y coordinate
        return: none
        """
        if (self.rect.x - characterX) > - 10 and (self.rect.x - characterX) < 10:
            pass
        elif self.rect.x < characterX: ## right
            self.rect.x += self.speed
            self.animation_folder = "assets/enemyAnimations/walkR"

        elif self.rect.x > characterX: ## left
            self.rect.x -= self.speed
            self.animation_folder = "assets/enemyAnimations/walkL"

        if (self.rect.y - characterY) > - 10 and (self.rect.y - characterY) < 10:
            pass
        elif self.rect.y < characterY:
            self.rect.y += self.speed
        elif self.rect.y > characterY:
            self.rect.y -= self.speed
