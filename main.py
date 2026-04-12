import pygame
from constants import *
# or import everything: from module_name import *
from logger import log_state



def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    #Initializing Pygame
    pygame.init()
    #this makes a clock object
    clock = pygame.time.Clock()
    #this defines the delta time variable
    dt = 0
    #defining how big the screen will be from "constants" file
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #making the game loop
    while(True):
        #This is what logs to our handy dandy logger function
        log_state()
        
        #this is what handles "game events" like, you know, closing it
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #pygame.Surface.fill("black")
        #pygame.Surface.fill(screen, (0,0,0)), I did this personally, because I could make it work, but it turns out you can do the line below
        screen.fill("black")
        #I have no idea what this line below this does
        pygame.display.flip()
        

        #Here, we are going to call the .tick method on the clock object, pass it 60, which is what is going to set us to 60 FPS
        dt = clock.tick(60) / 1000
        






if __name__ == "__main__":
    main()
