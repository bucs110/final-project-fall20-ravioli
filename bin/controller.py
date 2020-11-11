import pygame
import bin.character
import bin.enemy
import bin.functions
import bin.melee

class Controller:
    def __init__(self):
        ##INITIALIZE SCREEN, SPRITES, AND STATE##
        self.display = pygame.display.set_mode((1500, 800), pygame.RESIZABLE)
        (self.upper_boundry, self.lower_boundry, self.left_boundry, self.right_boundry) = (100, 700, 100, 1400)

        self.character = bin.character.Character((100, 100), "assets/resized_ravioli.png")
        self.enemy = bin.enemy.Enemy((800, 400), 10, "assets/ramsay.png")
        self.enemy2 = bin.enemy.Enemy((400, 400), 50, "assets/ramsay.png")


        self.STATE = "gameplay"

        ##ESTABLISH SPRITE GROUPS##
        self.all_sprites = pygame.sprite.Group( (self.character, self.enemy, self.enemy2) )
        self.all_enemies = pygame.sprite.Group(self.enemy, self.enemy2)
        self.weapons = ()

    def mainloop(self):
        while True:
            if self.STATE == "gameplay":
                self.gameloop()
            elif self.STATE == "exit":
                self.exitloop()

    def gameloop(self):
        (up, down, left, right, sword, sword_cooldown) = (False, False, False, False, 50, 50)
        clock = pygame.time.Clock()

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
                        if sword == sword_cooldown:
                            self.sword = bin.melee.Melee(70, "assets/resizedd_penne_sword_vertical.png")
                            self.sword.add((self.weapons, self.all_sprites))

                            self.sword.strike(self.character.givePosition())
                            enemy_got_hit = pygame.sprite.spritecollide(self.sword, self.all_enemies, False)
                            for i in enemy_got_hit:
                                enemy_life_status = i.gotHit()
                                if enemy_life_status == "dead":
                                    i.kill()
                                if enemy_life_status == "alive":
                                    i.knockBack(self.upper_boundry, self.lower_boundry, self.right_boundry, self.left_boundry, self.character.givePosition())
                            sword = 0


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
                        #self.sword.kill()

            ## ACTUAL CHARACTER MOVEMENT ##
            ##change to elif statements to disable diagnoal movement##
            if up:
                self.character.moveUp(self.upper_boundry)
            if down:
                self.character.moveDown(self.lower_boundry)
            if left:
                self.character.moveLeft(self.left_boundry)
            if right:
                self.character.moveRight(self.right_boundry)

            ## DETECTING IF PLAYER IS HIT AND DOING DAMAGE ##
            player_get_hit = pygame.sprite.spritecollide(self.character, self.all_enemies, False)
            if len(player_get_hit) > 0:
                player_life = self.character.gotHit()
                if player_life == "dead":
                    self.character.kill()
                    self.STATE = "exit"
                elif player_life == "alive":
                    self.character.knockBack(self.upper_boundry, self.lower_boundry, self.right_boundry, self.left_boundry) ##maybe do some editing to make smoother##


            ## This should make enemies turn around when they collide but its untested, bad, and not really needed ##
            enemy_collision = pygame.sprite.groupcollide(self.all_enemies, self.all_enemies, False, False)
            if len(enemy_collision) >= 4:
                for i in enemy_collision:
                    i.switchDirection()



            ##SCREEN UPDATES##
            self.all_sprites.update()
            self.display.fill((100, 15, 69))
            self.all_sprites.draw(self.display)
            pygame.display.flip()

            ## Check how long the sword has been out and kill over 30 ticks ##
            if sword < sword_cooldown:
                sword += 1
                if sword == sword_cooldown:
                    self.sword.kill()

            ##SET FPS##
            clock.tick(500)

    def exitloop(self):
        pygame.quit()
        exit()
