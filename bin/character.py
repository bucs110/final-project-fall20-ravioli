import pygame
import bin.functions

class Character(pygame.sprite.Sprite):
    def __init__(self, position, filename, boundaries):
        """
        initialzes the user's character and its position, image, boundaries, and fighting stats and abilities
        Args:
        position --> (touple) the character's (x,y) coordinates
        filename --> (str) the name of the file of the character's image
        boundaries --> (touple) the limits to where the character can move
        return: none
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
        self.attack_cooldown = 0
        self.got_hit_cooldown = 0
        self.total_money = 2000
        self.upgrade_level = 1
        self.upgrade_color = "orange"

        self.damage_output = 5

        ## animation variables ##
        self.animation_frame = "idleR1.png"
        self.current_iteration = 0
        self.frame = 0
        self.animation_folder = "assets/" + self.upgrade_color + "KnightAnimations/idleR"
        self.animation_rate = 2

    def moveUp(self):
        """
        Moves the character upwards
        Args: none
        Return: none
        """
        if self.STATE  == "movement":
            if self.rect.y > self.upper_boundry:
                self.rect.y -= self.speed
            self.direction = "up"
            self.animation_folder = "assets/" + self.upgrade_color + "KnightAnimations/walkU"


    def moveDown(self):
        """
        Moves the character downwards
        Args: none
        Return: None
        """
        if self.STATE  == "movement":
            if self.rect.y < self.lower_boundry:
                self.rect.y += self.speed
            self.direction = "down"
            self.animation_folder = "assets/" + self.upgrade_color + "KnightAnimations/walkD"

    def moveRight(self):
        """
        Moves the character right
        Args: none
        Return: none
        """
        if self.STATE  == "movement":
            if self.rect.x < self.right_boundry:
                self.rect.x += self.speed
            self.direction = "right"
            self.animation_folder = "assets/" + self.upgrade_color + "KnightAnimations/walkR"

    def moveLeft(self):
        """
        Moves the character left
        Args: none
        Return: none
        """
        if self.STATE  == "movement":
            if self.rect.x > self.left_boundry:
                self.rect.x -= self.speed
            self.direction = "left"
            self.animation_folder = "assets/" + self.upgrade_color + "KnightAnimations/walkL"

    def gotHit(self):
        """
        used to reduce the health of the character by 10 when it gets hit and determines if the character
        is alive or dead by its amount of health left
        Args: None
        Return: "alive" (str) character is still alive and some health remains
                "dead" (str) character is dead and all health is gone
        """
        if self.got_hit_cooldown == 0:
            self.health -= 10
        #print(str(self.health) + " character")
        if self.health == 0:
            return "dead"
        else:
            return "alive"


    def knockBack(self):
        """
        Knocks back the character 75 pixels in the opposite direction after being hit or until it hits the
        boundary if it would otherwise go out of frame
        Args: None
        Return: None
        """
        self.STATE = "knockback"
        self.got_hit_cooldown = 5 * self.animation_rate
        self.current_iteration = 0

        bounce_back = 75
        self.direction = bin.functions.makeOppositeDirections(self.direction)
        if self.direction == "up":
            self.animation_folder = "assets/" + self.upgrade_color + "KnightAnimations/damageD"
            self.rect.y -= bounce_back
            if self.rect.y < self.upper_boundry:
                self.rect.y = self.upper_boundry
        elif self.direction == "down":
            self.animation_folder = "assets/" + self.upgrade_color + "KnightAnimations/damageU"
            self.rect.y += bounce_back
            if self.rect.y > self.lower_boundry:
                self.rect.y = self.lower_boundry
        elif self.direction == "right":
            self.animation_folder = "assets/" + self.upgrade_color + "KnightAnimations/damageL"
            self.rect.x += bounce_back
            if self.rect.x > self.right_boundry:
                self.rect.x = self.right_boundry
        elif self.direction == "left":
            self.animation_folder = "assets/" + self.upgrade_color + "KnightAnimations/damageR"
            self.rect.x -= bounce_back
            if self.rect.x < self.left_boundry:
                self.rect.x = self.left_boundry
        self.direction = bin.functions.makeOppositeDirections(self.direction)

    def givePosition(self):
        """
        get the current position and direction of the character
        args: None
        Return: self.rect.x, self.rect.y, self.direction (touple) the characters position and direction
        """
        return (self.rect.x, self.rect.y, self.direction)

    def attackMode(self):
        """
        changes the state of the character to attack and gives the character a cool down after it attacks
        Args: none
        Return: None
        """
        self.STATE = "attack"
        self.current_iteration = 0
        self.attack_cooldown = 8 * self.animation_rate
        if self.direction == "right":
            self.animation_folder = "assets/" + self.upgrade_color + "KnightAnimations/attackR"
        elif self.direction == "left":
            self.animation_folder = "assets/" + self.upgrade_color + "KnightAnimations/attackL"
        elif self.direction == "up":
            self.animation_folder = "assets/" + self.upgrade_color + "KnightAnimations/attackU"
        elif self.direction == "down":
            self.animation_folder = "assets/" + self.upgrade_color + "KnightAnimations/attackD"


    def idleMode(self):
        """
        Uses the animation folder to make the character look idle if the character is idle
        Args: None
        Return: None
        """
        if self.STATE  == "movement":
            if self.direction == "right":
                self.animation_folder = "assets/" + self.upgrade_color + "KnightAnimations/idleR"
            elif self.direction == "left":
                self.animation_folder = "assets/" + self.upgrade_color + "KnightAnimations/idleL"
            elif self.direction == "up":
                self.animation_folder = "assets/" + self.upgrade_color + "KnightAnimations/idleU"
            elif self.direction == "down":
                self.animation_folder = "assets/" + self.upgrade_color + "KnightAnimations/idleD"

    def update(self):
        """
        Updates the model for a single frame
        Args: None
        Return: None
        """
        #print(self.attack_cooldown, self.got_hit_cooldown)
        if self.attack_cooldown == 0 and self.got_hit_cooldown == 0:
            self.STATE = "movement"


        self.current_iteration = bin.functions.currentIterationChecker(self.current_iteration, self.animation_folder)
        (self.animation_frame, self.current_iteration, self.frame) = bin.functions.animate(self.animation_folder, self.animation_rate, self.current_iteration, self.frame, self.animation_frame)
        self.image = pygame.transform.smoothscale(pygame.image.load(self.animation_folder + "/" + self.animation_frame).convert_alpha(), (100, 100))
        temporary = self.image.get_rect()
        temporary.x = self.rect.x
        temporary.y = self.rect.y
        self.rect = temporary

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        if self.got_hit_cooldown > 0:
            self.got_hit_cooldown -= 1
