import pygame
import bin.character
import bin.enemy
import bin.functions
import bin.melee
import bin.merchant
import bin.button
import os
import time

class Controller:
    def __init__(self):
        """
        Initializes the screen and the main variables
        args: none
        """

        pygame.font.init()
        ##INITIALIZE SCREEN, SPRITES, AND STATE##
        self.display = pygame.display.set_mode((1500, 800), pygame.RESIZABLE)
        (self.upper_boundry, self.lower_boundry, self.left_boundry, self.right_boundry) = (100, 700, 100, 1400)
        self.boundaries = (self.upper_boundry, self.lower_boundry, self.left_boundry, self.right_boundry)

        self.character = bin.character.Character((100, 100), "assets/resized_ravioli.png", self.boundaries)
        self.merchant_upgrade = bin.merchant.Merchant((200, 200), "assets/merchant.png", "upgrade")

        self.swing = 0
        self.STATE = "gameplay"
        self.current_wave = 0
        self.wave_list = os.listdir("etc")
        self.wave = "etc/" + str(self.wave_list[self.current_wave])
        print(self.wave_list)
        self.enemy_spawn_time = 100
        self.enemy_number = 0

        ##ESTABLISH SPRITE GROUPS##
        self.all_sprites = pygame.sprite.Group( (self.character, self.merchant_upgrade) )
        self.all_enemies = pygame.sprite.Group()
        self.weapons = pygame.sprite.Group()
        self.wave_reset = pygame.sprite.Group()

        ##ESTALBISH IMPORTANT TEXT##
        self.health_font = pygame.font.SysFont('Times New Roman', 50)
        self.money_font = pygame.font.SysFont('Times New Roman', 50)
        self.wave_font = pygame.font.SysFont('Times New Roman', 50)

    def mainloop(self):
        """
        Determines which loops of the game should run
        args: none
        return: none
        """
        while True:
            if self.STATE == "menu":
                pass
            elif self.STATE == "gameplay":
                self.gameloop()
            elif self.STATE == "exit":
                self.exitloop()
            elif self.STATE == "nextWave":
                self.nextWave()
            elif self.STATE == "winScreen":
                pass
            elif self.STATE == "loseScreen":
                pass

    def gameloop(self):
        """
        Main loop of the gameplay where the character can move and fight
        Args: none
        Return: none
        """
        (up, down, left, right, reset_click, sword, sword_cooldown) = (False, False, False, False, False, 50, 50)
        clock = pygame.time.Clock()
        with open(self.wave, 'r') as file:
            information = file.readlines()
            self.total_wave_enemies = len(information) // 6

        ## EVENT LOOP ##
        while self.STATE == "gameplay":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.STATE = "exit"

                if event.type == pygame.KEYDOWN:
                    ##MOVEMENT TOGGLES##
                    if event.key == pygame.K_w:
                        up = True
                    if event.key == pygame.K_d:
                        right = True
                    if event.key == pygame.K_a:
                        left = True
                    if event.key == pygame.K_s:
                        down = True
                    if event.key == pygame.K_LCTRL:
                        self.STATE = "exit"
                    if event.key == pygame.K_SPACE:
                        if self.swing == 0:
                            self.character.attackMode()
                            sword_swoosh = pygame.mixer.Sound("assets/sounds/attackSound.wav")
                            sword_swoosh.play()
                            self.swing += 1
                    if event.key == pygame.K_e:
                        reset_click = True


                if event.type == pygame.KEYUP:
                    ##MOVEMENT TOGGLES##
                    if event.key == pygame.K_w:
                        up = False
                    if event.key == pygame.K_d:
                        right = False
                    if event.key == pygame.K_a:
                        left = False
                    if event.key == pygame.K_s:
                        down = False
                    if event.key == pygame.K_SPACE:
                        pass
                    if event.key == pygame.K_e:
                        reset_click = False

            ## SPAWNING ENEMIES ##
            if self.enemy_spawn_time > 0:
                self.enemy_spawn_time -= 1
            elif self.enemy_spawn_time == 0 and self.enemy_number != self.total_wave_enemies:
                self.enemy = bin.functions.spawnEnemy(self.wave, self.boundaries, self.enemy_number)
                self.all_enemies.add(self.enemy)
                self.all_sprites.add(self.enemy)
                self.enemy_spawn_time = 100
                self.enemy_number += 1
            #print(self.enemy_spawn_time, self.total_wave_enemies, self.enemy_number)

            ## WAVE CHECKER ##
            if self.enemy_spawn_time == 0 and len(self.all_enemies) == 0 and self.enemy_number == self.total_wave_enemies:
                if len(self.wave_reset) == 0:
                    self.wave_lever = bin.button.Button((700, 400), "assets/waveLever.png")
                    self.all_sprites.add(self.wave_lever)
                    self.wave_reset.add(self.wave_lever)
                else:
                    if reset_click:
                        reset_contact = pygame.sprite.spritecollide(self.character, self.wave_reset, False, pygame.sprite.collide_circle_ratio(self.character.hit_ratio))
                        if reset_contact:
                            ##ADVANCE TO NEXT WAVE##
                            self.wave_lever.toggle("assets/waveLeverFlipped.png")
                            self.enemy_number = 0
                            self.STATE = "nextWave"


            ## There are a bit of hardcoded values / magic numbers here but I just wanted to get it working ##
            if self.swing > 0:
                if self.swing > 10 and self.swing < 12:
                    sword_swing = pygame.sprite.spritecollide(self.character, self.all_enemies, False, pygame.sprite.collide_circle_ratio(self.character.hit_ratio))
                    for e in sword_swing:
                        e.knockBack(self.character.direction)
                        if e.gotHit() == "dead":
                            self.character.total_money += e.reward_money
                            e.kill()
                        print(self.character.total_money)
                self.swing += 1
            if self.swing > 16:
                self.swing = 0

            ## ACTUAL CHARACTER MOVEMENT ##
            ##change to elif statements to disable diagnoal movement##
            if up:
                self.character.moveUp()
            if down:
                self.character.moveDown()
            if left:
                self.character.moveLeft()
            if right:
                self.character.moveRight()
            if not up and not down and not left and not right:
                self.character.idleMode()


            ## DETECTING IF PLAYER IS HIT AND DOING DAMAGE ##
            player_get_hit = pygame.sprite.spritecollide(self.character, self.all_enemies, False)
            if len(player_get_hit) > 0:
                player_life = self.character.gotHit()
                if player_life == "dead":
                    self.character.kill()
                    self.STATE = "exit"
                elif player_life == "alive":
                    self.character.knockBack() ##maybe do some editing to make smoother##
                    character_hit_sound = pygame.mixer.Sound("assets/sounds/playerHit.wav")
                    character_hit_sound.play()


            ##TEXT UPDATES##
            health_display = self.health_font.render("Health: " + str(self.character.health), False, (255, 14, 14))
            money_display = self.health_font.render("Money: " + str(self.character.total_money), False, (24, 188, 40))
            wave_display = self.health_font.render("Wave: " + str(self.current_wave + 1), False, (255, 255, 255))


            ##SCREEN UPDATES##
            self.all_sprites.update()
            self.display.fill((0, 0, 0)) #139 244 255

            self.display.blit(health_display, (210,0))
            self.display.blit(money_display, (610,0))
            self.display.blit(wave_display, (1010,0))

            self.all_sprites.draw(self.display)
            pygame.display.flip()


            ##SET FPS##
            clock.tick(30)
            #print(self.swing)

    def nextWave(self):
        """
        In-between screen that changes to the next wave
        args: none
        return: none
        """
        time.sleep(1)
        self.wave_lever.kill()
        if self.current_wave + 1 < len(self.wave_list):
            self.current_wave += 1
            self.wave = "etc/" + str(self.wave_list[self.current_wave])
            self.STATE = "gameplay"
        elif self.current_wave == len(self.wave_list):
            self.STATE == "winScreen"


    def exitloop(self):
        """
        Closes the game
        Args: none
        Return: none
        """
        pygame.quit()
        exit()
