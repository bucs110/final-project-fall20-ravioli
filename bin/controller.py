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


        self.swing = 0
        self.STATE = "start"
        self.current_wave = 0
        self.wave_list = os.listdir("assets/waves")
        self.wave = "assets/waves/" + str(self.wave_list[self.current_wave])
        #print(self.wave_list)
        self.enemy_spawn_time = 100
        self.enemy_number = 0

        ##ESTABLISH SPRITE GROUPS##
        self.all_sprites = pygame.sprite.Group( (self.character) )
        self.all_enemies = pygame.sprite.Group()
        self.weapons = pygame.sprite.Group()
        self.wave_reset = pygame.sprite.Group()
        self.merchants = pygame.sprite.Group()
        self.sale_items = pygame.sprite.Group()

        ##ESTABLISH IMPORTANT TEXT##
        self.health_font = pygame.font.Font('assets/customFont.ttf', 50)
        self.money_font = pygame.font.Font('assets/customFont.ttf', 50)
        self.wave_font = pygame.font.Font('assets/customFont.ttf', 50)
        self.complete_font = pygame.font.Font('assets/customFont.ttf', 50)
        self.lever_font = pygame.font.Font('assets/customFont.ttf', 20)

        ##ESTABLISH BUTTON LOCATIONS##
        self.button_size = (250, 64)
        self.health_button_location = (629, 80)
        self.upgrade_button_location = (329, 80)
        self.speed_button_location = (929, 80)

    def mainloop(self):
        """
        Determines which loops of the game should run
        args: none
        return: none
        """
        while True:
            if self.STATE == "start":
                self.startloop()
            elif self.STATE == "gameplay":
                self.gameloop()
            elif self.STATE == "exit":
                self.exitloop()
            elif self.STATE == "nextWave":
                self.nextWave()
            elif self.STATE == "victory":
                self.victory()
            elif self.STATE == "loseScreen":
                self.loseScreen()

    def startloop(self):
        """
        displays the starting screen
        args: none
        return: none
        """
        self.background = bin.button.Button((0, 0), "assets/gui_design_screen.jpg", "null", (1500, 800))

        while self.STATE == "start":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.STATE = "exit"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                    	self.STATE = "gameplay"

            self.display.fill((255, 255, 255))
            self.display.blit(self.background.image, self.background.rect)
            pygame.display.flip()

    def gameloop(self):
        """
        Main loop of the gameplay where the character can move and fight
        Args: none
        Return: none
        """
        ## reading from json file when starting the game to get the past high score
        #fileref = open ("highScore.json","r")
        #score = json.load(fileref)
        self.background = bin.button.Button((0, 0), "assets/dungeonArena.jpg", "null", (1500, 800))
        (up, down, left, right, reset_click, sword, sword_cooldown) = (False, False, False, False, False, 50, 50)
        clock = pygame.time.Clock()
        with open(self.wave, 'r') as file:
            information = file.readlines()
            self.total_wave_enemies = len(information) // 6

        if len(self.merchants) == 0:
            wave_complete_display = self.complete_font.render("", False, (255, 255, 0))
            lever_display = self.lever_font.render("", False, (255, 255, 255))

        pygame.mixer.music.load('assets/music/waveMusic.wav')
        pygame.mixer.music.play(-1)

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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.sale_items:
                        for e in self.sale_items:
                            if e.rect.collidepoint(event.pos):
                                if e.use == "health":
                                    if self.character.health < 100 and self.character.total_money >= 10:
                                        self.character.total_money -= 10
                                        self.character.health += 10
                                    if self.character.health == 100:
                                        e.kill()
                                        self.health_button = bin.button.Button(self.health_button_location, "assets/maxed_out.png", "null", self.button_size)
                                        self.sale_items.add(self.health_button)
                                        self.all_sprites.add(self.health_button)
                                if e.use == "upgrade_ii":
                                    if self.character.upgrade_level == 1 and self.character.total_money >= 250:
                                        self.character.total_money -= 250
                                        self.character.upgrade_level += 1
                                        self.character.damage_output = 10
                                        self.character.upgrade_color = "cyan"
                                        e.kill()
                                        self.tier_iii_upgrade = bin.button.Button(self.upgrade_button_location, "assets/upgrade_iii.png", "upgrade_iii", self.button_size)
                                        self.sale_items.add(self.tier_iii_upgrade)
                                        self.all_sprites.add(self.tier_iii_upgrade)
                                if e.use == "upgrade_iii":
                                    if self.character.upgrade_level == 2 and self.character.total_money >= 500:
                                        self.character.total_money -= 500
                                        self.character.upgrade_level += 1
                                        self.character.damage_output = 20
                                        self.character.upgrade_color = "pink"
                                        e.kill()
                                        self.maxed_out = bin.button.Button(self.upgrade_button_location, "assets/maxed_out.png", "null", self.button_size)
                                        self.sale_items.add(self.maxed_out)
                                        self.all_sprites.add(self.maxed_out)
                                if e.use == "speed_1":
                                    if self.character.speed == 3 and self.character.total_money >= 50:
                                        self.character.total_money -= 50
                                        self.character.speed += 2
                                        e.kill()
                                        self.speed_button = bin.button.Button(self.speed_button_location, "assets/speed_2.png", "speed_2", self.button_size)
                                        self.sale_items.add(self.speed_button)
                                        self.all_sprites.add(self.speed_button)
                                if e.use == "speed_2":
                                    if self.character.speed == 5 and self.character.total_money >= 100:
                                        self.character.total_money -= 100
                                        self.character.speed += 2
                                        e.kill()
                                        self.maxed_out = bin.button.Button(self.speed_button_location, "assets/maxed_out.png", "null", self.button_size)
                                        self.sale_items.add(self.maxed_out)
                                        self.all_sprites.add(self.maxed_out)

                            else:
                                pass


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

                    ## WAVE ENDING ##
                    pygame.mixer.music.stop()
                    wave_complete_display = self.complete_font.render("Wave " + str(self.current_wave + 1) + "  Complete!", False, (255, 255, 0))
                    self.display.blit(wave_complete_display, (575, 200))
                    pygame.display.flip()
                    next_wave_sound = pygame.mixer.Sound("assets/sounds/endRoundSound.wav")
                    next_wave_sound.play()
                    time.sleep(5)

                    ## CREATE MERCHANTS AND LEVERS ##
                    pygame.mixer.music.load('assets/music/upgradeMusic.wav')
                    pygame.mixer.music.play(-1)
                    wave_complete_display = self.complete_font.render("Walk up to merchants and click the buttons to upgrade.", False, (255, 255, 0))
                    lever_display = self.lever_font.render("Press [ e ] to start the next wave", False, (255, 255, 255))
                    self.wave_lever = bin.button.Button((700, 400), "assets/waveLever.png", "null", (50,50))
                    self.upgrade_merchant = bin.merchant.Merchant((399, 150), "assets/merchantAnimations/gold", "upgrade")
                    self.health_merchant = bin.merchant.Merchant((699, 150), "assets/merchantAnimations/red", "health")
                    self.speed_merchant = bin.merchant.Merchant((999, 150), "assets/merchantAnimations/blue", "speed")
                    self.all_sprites.add(self.wave_lever, self.upgrade_merchant, self.health_merchant, self.speed_merchant)
                    self.wave_reset.add(self.wave_lever)
                    self.merchants.add(self.upgrade_merchant, self.health_merchant, self.speed_merchant)
                else:
                    if reset_click:
                        reset_contact = pygame.sprite.spritecollide(self.character, self.wave_reset, False, pygame.sprite.collide_circle_ratio(self.character.hit_ratio))
                        if reset_contact:
                            ##ADVANCE TO NEXT WAVE##
                            pygame.mixer.music.stop()
                            self.wave_lever.toggle("assets/waveLeverFlipped.png")
                            self.enemy_number = 0
                            self.STATE = "nextWave"


            ## MERCHANT INTERACTIONS ##
            if self.merchants:
                conversation = pygame.sprite.spritecollide(self.character, self.merchants, False, pygame.sprite.collide_circle_ratio(1.0))
                #print(conversation)
                if conversation:
                    for merch in conversation:
                        if merch.type == "upgrade":
                            if self.sale_items:
                                pass
                            elif self.character.upgrade_level == 1:
                                self.tier_ii_upgrade = bin.button.Button(self.upgrade_button_location, "assets/upgrade_ii.png", "upgrade_ii", self.button_size)
                                self.sale_items.add(self.tier_ii_upgrade)
                                self.all_sprites.add(self.tier_ii_upgrade)
                            elif self.character.upgrade_level == 2:
                                self.tier_iii_upgrade = bin.button.Button(self.upgrade_button_location, "assets/upgrade_iii.png", "upgrade_iii", self.button_size)
                                self.sale_items.add(self.tier_iii_upgrade)
                                self.all_sprites.add(self.tier_iii_upgrade)
                            elif self.character.upgrade_level == 3:
                                self.maxed_out = bin.button.Button(self.upgrade_button_location, "assets/maxed_out.png", "null", self.button_size)
                                self.sale_items.add(self.maxed_out)
                                self.all_sprites.add(self.maxed_out)

                        elif merch.type == "health":
                            if self.sale_items:
                                pass
                            elif self.character.health < 100:
                                self.health_button = bin.button.Button(self.health_button_location, "assets/heth_button.png", "health", self.button_size)
                                self.sale_items.add(self.health_button)
                                self.all_sprites.add(self.health_button)
                            elif self.character.health == 100:
                                self.health_button = bin.button.Button(self.health_button_location, "assets/maxed_out.png", "null", self.button_size)
                                self.sale_items.add(self.health_button)
                                self.all_sprites.add(self.health_button)
                        elif merch.type == "speed":
                            if self.sale_items:
                                pass
                            elif self.character.speed == 3:
                                self.speed_button = bin.button.Button(self.speed_button_location, "assets/speed_1.png", "speed_1", self.button_size)
                                self.sale_items.add(self.speed_button)
                                self.all_sprites.add(self.speed_button)
                            elif self.character.speed == 5:
                                self.speed_button = bin.button.Button(self.speed_button_location, "assets/speed_2.png", "speed_2", self.button_size)
                                self.sale_items.add(self.speed_button)
                                self.all_sprites.add(self.speed_button)
                            elif self.character.speed == 7:
                                self.maxed_out = bin.button.Button(self.speed_button_location, "assets/maxed_out.png", "null", self.button_size)
                                self.sale_items.add(self.maxed_out)
                                self.all_sprites.add(self.maxed_out)

            ## CHECKS TO SEE IF THE CONVERSATIONS HAVE STOPPED ##
            if self.merchants:
                if conversation == []:
                    #print("this is being read")
                    for e in self.sale_items:
                        e.kill()


            ## There are a bit of hardcoded values / magic numbers here but I just wanted to get it working ##
            if self.swing > 0:
                if self.swing > 10 and self.swing < 12:
                    sword_swing = pygame.sprite.spritecollide(self.character, self.all_enemies, False, pygame.sprite.collide_circle_ratio(self.character.hit_ratio))
                    for e in sword_swing:
                        e.knockBack(self.character.direction)
                        if e.gotHit(self.character.damage_output) == "dead":
                            self.character.total_money += e.reward_money
                            e.kill()
                        #print(self.character.total_money)
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
            player_get_hit = pygame.sprite.spritecollide(self.character, self.all_enemies, False, pygame.sprite.collide_rect_ratio(.65))
            if len(player_get_hit) > 0:
                player_life = self.character.gotHit()
                if player_life == "dead":
                    self.character.kill()
                    self.STATE = "loseScreen"
                elif player_life == "alive":
                    self.character.knockBack() ##maybe do some editing to make smoother##
                    character_hit_sound = pygame.mixer.Sound("assets/sounds/playerHitSound.wav")
                    character_hit_sound.play()


            ##TEXT UPDATES##
            health_display = self.health_font.render("Health: " + str(self.character.health), False, (255, 14, 14))
            money_display = self.health_font.render("Money: " + str(self.character.total_money), False, (24, 188, 40))
            wave_display = self.health_font.render("Wave: " + str(self.current_wave + 1), False, (255, 255, 255))


            ##SCREEN UPDATES##
            self.all_sprites.update()
            self.display.fill((255, 255, 255))
            self.display.blit(self.background.image, self.background.rect)

            self.display.blit(health_display, (360, 10))
            self.display.blit(money_display, (645, 10))
            self.display.blit(wave_display, (980, 10))
            self.display.blit(wave_complete_display, (300, 730))
            self.display.blit(lever_display, (625, 450))

            for e in self.all_enemies:
                e.getCharacterCoords(self.character.givePosition())
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
        time.sleep(.5)
        for e in self.merchants:
            e.kill()
        self.wave_lever.kill()
        if self.current_wave + 1 <= len(self.wave_list):
            self.current_wave += 1
            if (self.current_wave) == len(self.wave_list):
                self.STATE = "victory"

            else:
                self.wave = "assets/waves/" + str(self.wave_list[self.current_wave])
                self.STATE = "gameplay"


    def victory(self):
        """
        displays the winning screen
        args: none
        return: none
        """
        self.background = bin.button.Button((0, 0), "assets/gui_design_victory.jpg", "null", (1500, 800))
        pygame.mixer.music.stop()
        victory_sound = pygame.mixer.Sound("assets/sounds/victorySound.wav")
        victory_sound.play()
        total_game_time = pygame.time.get_ticks()
        print(bin.functions.convertTime(total_game_time))
        while self.STATE == "victory":
            ## here check if new score object needs to be updated with the changeScore method in score class

            ## if it is a new high score, write to the json file with the score that is in the highScore object from score class
            #fileref = open("highScore.json","w")
            #json.dump(newScore.__dict__, fileref)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.STATE = "exit"

            self.display.fill((255, 255, 255))
            self.display.blit(self.background.image, self.background.rect)
            pygame.display.flip()

    def loseScreen(self):
        """
        displays the winning screen
        args: none
        return: none
        """
        self.background = bin.button.Button((0, 0), "assets/gui_design_lose.jpg", "null", (1500, 800))
        pygame.mixer.music.stop()
        game_over_sound = pygame.mixer.Sound("assets/sounds/failureSound.wav")
        game_over_sound.play()
        while self.STATE == "loseScreen":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.STATE = "exit"

            self.display.fill((255, 255, 255))
            self.display.blit(self.background.image, self.background.rect)
            pygame.display.flip()

    def exitloop(self):
        """
        Closes the game
        Args: none
        Return: none
        """
        pygame.quit()
        exit()
