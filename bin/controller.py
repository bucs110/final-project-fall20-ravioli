import pygame
import bin.character

class Controller:
    def __init__(self):
        self.display = pygame.display.set_mode((1500, 800), pygame.RESIZABLE)
        self.character = bin.character.Character((100, 100), "assets/resized_ravioli.png")
        self.STATE = "gameplay"

    def mainloop(self):
        while True:
            if self.STATE == "gameplay":
                self.gameloop()
            elif self.STATE == "exit":
                self.exitloop()

    def gameloop(self):
        up = False
        down = False
        right = False
        left = False

        while self.STATE == "gameplay":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.STATE = "exit"

                ##BUTTON HELD MOVEMENT##
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        up = True
                    if event.key == pygame.K_d:
                        right = True
                    if event.key == pygame.K_a:
                        left = True
                    if event.key == pygame.K_s:
                        down = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        up = False
                    if event.key == pygame.K_d:
                        right = False
                    if event.key == pygame.K_a:
                        left = False
                    if event.key == pygame.K_s:
                        down = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if(self.character.rect.collidepoint(event.position)):
                        self.STATE = "exit"

            if up:
                self.character.moveUp()
            elif down:
                self.character.moveDown()
            elif left:
                self.character.moveLeft()
            elif right:
                self.character.moveRight()

            self.character.update()
            self.display.fill((100, 15, 69))
            self.display.blit(self.character.image, (self.character.rect.x, self.character.rect.y))
            pygame.display.flip()

    def exitloop(self):
        pygame.quit()
        exit()
