"""Functions about game control"""
import sys
import pygame


def handle_keydown_event(event, ship):
    """if any key is pressed, then handle it"""
    if event.key == pygame.K_RIGHT:
        # pressed ~ switch on
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True


def handle_keyup_event(event, ship):
    """if any key is released, then handle it"""
    if event.key == pygame.K_RIGHT:
        # released ~ switch off
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ship):
    """react on events"""
    # handle events in event_list
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            handle_keydown_event(event, ship)
        elif event.type == pygame.KEYUP:
            handle_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship):
    """update screen background & elements"""
    # draw the background
    screen.fill(ai_settings.bg_color)
    # draw the ship
    ship.blit_me()

    # update display
    pygame.display.flip()
