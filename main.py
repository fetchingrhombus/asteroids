import pygame
from constants import *
# or import everything: from module_name import *
from logger import log_state



def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    while(True):
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #pygame.Surface.fill("black")
        #pygame.Surface.fill(screen, (0,0,0)), I did this personally, because I could make it work, but it turns out you can do the line below
        screen.fill("black")
        #I have no idea what this line below this does
        pygame.display.flip()






if __name__ == "__main__":
    main()
