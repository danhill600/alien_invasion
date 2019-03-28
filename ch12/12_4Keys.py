#12-4. Keys: Make a Pygame file that creates an empty screen. In the event
#loop, print the event.key attribute whenever a pygame.KEYDOWN event is detected.
#Run the program and press various keys to see how Pygame responds.
import pygame
import time
def message_display(text,screen):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    screen.blit(TextSurf,TextRect)
    pygame.display.update()

    time.sleep(2)

#    run_game()

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def check_events(screen):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            print(str(event.key))
            message_display(str(event.key),screen)


#        elif event.type == pygame.KEYUP:
#            check_keyup_events(event, ship)

def run_game():
    #initialize game and create a screen object.
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(
        (800, 800))



    #Start the main loop for the game.
    while True:
        screen.fill((137, 60, 178))
        check_events(screen)
        pygame.display.flip()




run_game()
