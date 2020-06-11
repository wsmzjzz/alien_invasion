import sys
import pygame
from settings import Settings
from ship import  Ship


def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
         ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # create a ship
    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            # print(event.type)
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        ship.blit_me()

        pygame.display.flip()


if __name__ == '__main__':
    run_game()
