#12-3. Rocket: Make a game that begins with a rocket in the center of the
#screen. Allow the player to move the rocket up, down, left, or right using the
#four arrow keys. Make sure the rocket never moves beyond any edge of the
#screen.

import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen

        #Load the ship image and get its rect
        self.image = pygame.image.load('rocket3.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen_rect

        #Start the ship at the middle of the screen 
        self.rect.centerx = self.screen.rect.centerx

        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flags."""
        #Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += 1

        if self.moving_left and self.rect.left > 0:
            self.center -= 1

        #then do up and down

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

def check_keydownevents(event, ship):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif even.key == pygame.K_DOWN:
        ship.moving_down = True

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.down == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyupevents(event, ship)

#def update_screen(screen, ship):
#    """Update images on the screen and flip to the new screen."""
#    #Redraw the screen during each pass through the loop
#    screen.fill()
#    ship.blitme()
#    pygame.display.flip()

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))

    ship = Ship(screen)

    while True:
        check_events(ship)
        ship.update()
        #update_screen(screen, ship)
        pygame.display.flip()

