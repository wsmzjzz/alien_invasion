"""Main entry of the alien invasion game"""
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()

    # game canvas
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
         ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # create a ship at center bottom
    ship = Ship(screen)

    while True:
        # mouse & keyboard events
        gf.check_events(ship)
        # update status (position, ...)
        ship.update(ai_settings)
        # re-draw all elements
        gf.update_screen(ai_settings, screen, ship)


if __name__ == '__main__':
    run_game()
