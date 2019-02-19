#12-3. Rocket: Make a game that begins with a rocket in the center of the
#screen. Allow the player to move the rocket up, down, left, or right using the
#four arrow keys. Make sure the rocket never moves beyond any edge of the
#screen.

import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('rocket3.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen_rect

def run_game():
    screen = pygame.display.set_mode(
        1200,800)

    ship =

