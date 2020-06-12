import sys
import pygame


def check_events():
    """react on events"""
    # handle events in event_list
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """update screen background & elements"""
    screen.fill(ai_settings.bg_color)
    ship.blit_me()

    pygame.display.flip()
