import pygame
from constants import *
# or import everything: from module_name import *
from logger import log_state
#importing from the player class code that we wrote
from player import Player




import pygame
from constants import *
# or import everything: from module_name import *
from logger import log_state
#importing from the player class code that we wrote
from player import Player




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
    #making the player appear on the screen, this puts him exactly in the middle of the screen
    Player.containers = (updatable, drawable)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    
import pygame
from constants import *
# or import everything: from module_name import *
from logger import log_state
#importing from the player class code that we wrote
from player import Player




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
    #Need to add the updatable and drawable, and containery bit *Before* I get the x and y guy in there
    #Updatable Group, Drawable Group
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    #Player is the name of the class, not an instance of it, This must be done before any players are created
    Player.containers = (updatable, drawable)


    #making the player appear on the screen, this puts him exactly in the middle of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    

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

        #I'm going to be updating the dude here so that he moves, this is how we moved the player before we added in groups to do so
        #player.update(dt)
        #Now that we have a group (with the player container, and the two groups) we will be moving the player through this instead.We use the updatable.update method to state "things that belong to the updatable group, need to call the .update method"
        updatable.update(dt)
        for objects in drawable:
            objects.draw(screen)

        #I'm going to repeat what I did above, but this time, for the drawables
        #drawable.update(dt)
       

       #attempting to draw the player, I'm doing this by calling the player class, with the method of "draw" and telling it to go to "screen"
        #This is where we are rendering the dude
        #We are commenting out the player.draw(screen) because we are changing how we draw to the screen with the updatable.update(dt) function call
        #player.draw(screen)
        #I have no idea what this line below this does, but it must be done after all other drawing commands
        pygame.display.flip()
        

        #Here, we are going to call the .tick method on the clock object, pass it 60, which is what is going to set us to 60 FPS. The divide by 1k is to convert up from miliseconds`
        dt = clock.tick(60) / 1000    #making the Updatable group
    updatable = pygame.sprite.Group()

    #making the drawable group
    drawable = pygame.sprite.Group()
    
    # Player is the name of the class, not an instance of it
    # This must be done before any Player objects are created
    
    
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

        #I'm going to be updating the dude here so that he moves, this is how we moved the player before we added in groups to do so
        #player.update(dt)
        #Now that we have a group (with the player container, and the two groups) we will be moving the player through this instead.We use the updatable.update method to state "things that belong to the updatable group, need to call the .update method"
        updatable.update(dt)
        for objects in drawable:
            objects.draw(screen)

        #I'm going to repeat what I did above, but this time, for the drawables
        #drawable.update(dt)
       

       #attempting to draw the player, I'm doing this by calling the player class, with the method of "draw" and telling it to go to "screen"
        #This is where we are rendering the dude
        player.draw(screen)
        #I have no idea what this line below this does, but it must be done after all other drawing commands
        pygame.display.flip()
        

        #Here, we are going to call the .tick method on the clock object, pass it 60, which is what is going to set us to 60 FPS. The divide by 1k is to convert up from miliseconds`
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()
