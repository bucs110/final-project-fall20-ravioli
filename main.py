#import your controller
import pygame
import bin.controller



def main():
    #Create an instance on your controller object
    pygame.init()
    #print("Software Lead is: Emily Greene")
    #print("Backend is: Josef Schindler")
    #print("Frontend is: Roman Raguso")

    game = bin.controller.Controller()
    game.mainloop()
main()
