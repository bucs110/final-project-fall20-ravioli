import pygame
import bin.character
import bin.enemy

class Controller:
    def __init__(self):
        ##INITIALIZE SCREEN, SPRITES, AND STATE##
        self.display = pygame.display.set_mode((1500, 800), pygame.RESIZABLE)
        self.character = bin.character.Character((100, 100), "assets/resized_ravioli.png")
        self.enemy = bin.enemy.Enemy((800, 400), "assets/ramsay.png")
        self.STATE = "gameplay"

        ##ESTABLISH SPRITE GROUPS##
        self.player_and_enemies = pygame.sprite.Group( (self.character, self.enemy) )
        self.all_enemies = pygame.sprite.Group(self.enemy)


    def mainloop(self):
        while True:
            if self.STATE == "gameplay":
                self.gameloop()
            elif self.STATE == "exit":
                self.exitloop()

    def gameloop(self):
        (up, down, left, right) = (False, False, False, False)
        clock = pygame.time.Clock()

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


            if up:
                self.character.moveUp()
            elif down:
                self.character.moveDown()
            elif left:
                self.character.moveLeft()
            elif right:
                self.character.moveRight()


            ##SCREEN UPDATES##
            self.player_and_enemies.update()
            self.display.fill((100, 15, 69))
            self.player_and_enemies.draw(self.display)
            pygame.display.flip()

            ##SET FPS##
            clock.tick(500)

    def exitloop(self):
        pygame.quit()
        exit()
