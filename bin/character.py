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

        self.speed = 3
        self.hit_ratio = 1.0
        self.health = 100
        self.cooldown_timer = 150 ## ~5 seconds ##
        self.attack_cooldown = 0

        ## animation variables ##
        self.animation_frame = "idleR1.png"
        self.current_iteration = 0
        self.frame = 0
        self.animation_folder = "assets/orangeKnightAnimations/idleR"

    def moveUp(self):
        """
        Moves the character upwards
        Args: none
        Return:None
        """
        if self.rect.y > self.upper_boundry:
            self.rect.y -= self.speed
        self.direction = "up"
        self.animation_folder = "assets/orangeKnightAnimations/walkU"


    def moveDown(self):
        """
        Moves the character upwards
        Args: none
        Return: None
        """
        if self.rect.y < self.lower_boundry:
            self.rect.y += self.speed
        self.direction = "down"
        self.animation_folder = "assets/orangeKnightAnimations/walkD"

    def moveRight(self):
        """
        Moves the character upwards
        Args: none
        Return: None
        """

        if self.rect.x < self.right_boundry:
            self.rect.x += self.speed
        self.direction = "right"
        self.animation_folder = "assets/orangeKnightAnimations/walkR"

    def moveLeft(self):
        """
        Moves the character upwards
        Args: none
        Return:None
        """
        if self.rect.x > self.left_boundry:
            self.rect.x -= self.speed
        self.direction = "left"
        self.animation_folder = "assets/orangeKnightAnimations/walkL"

    def gotHit(self):
        """
        used to reduce the health of the character when it gets hit
        Args: None
        Return: (str) alive or dead
        """
        if self.cooldown_timer == 0:
            self.health -= 10
            self.cooldown_timer = 90 ## resets cooldown_timer ~3 seconds ##
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
        self.attack_cooldown = 11
        if self.direction == "right":
            self.animation_folder = "assets/orangeKnightAnimations/attackR"
        elif self.direction == "left":
            self.animation_folder = "assets/orangeKnightAnimations/attackL"
        elif self.direction == "up":
            self.animation_folder = "assets/orangeKnightAnimations/attackU"
        elif self.direction == "down":
            self.animation_folder = "assets/orangeKnightAnimations/attackD"


    def idleMode(self):
        """
        Changes the animation folder if the character is idle
        Args: None
        Return: None
        """
        if self.direction == "right":
            self.animation_folder = "assets/orangeKnightAnimations/idleR"
        elif self.direction == "left":
            self.animation_folder = "assets/orangeKnightAnimations/idleL"
        elif self.direction == "up":
            self.animation_folder = "assets/orangeKnightAnimations/idleU"
        elif self.direction == "down":
            self.animation_folder = "assets/orangeKnightAnimations/idleD"

    def update(self):
        """
        Updates the model for a single frame
        Args: None
        Return: None
        """
        if self.attack_cooldown == 0:
            self.STATE = "movement"


        self.current_iteration = bin.functions.currentIterationChecker(self.current_iteration, self.animation_folder)
        (self.animation_frame, self.current_iteration, self.frame) = bin.functions.animate(self.animation_folder, 2, self.current_iteration, self.frame, self.animation_frame)
        self.image = pygame.transform.smoothscale(pygame.image.load(self.animation_folder + "/" + self.animation_frame).convert_alpha(), (100, 100))
        temporary = self.image.get_rect()
        temporary.x = self.rect.x
        temporary.y = self.rect.y
        self.rect = temporary

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1
