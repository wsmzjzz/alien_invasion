"""Functions about game control"""
import sys
import pygame
from bullet import Bullet


def handle_keydown_event(event, ai_settings, screen, ship, bullets):
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
    elif event.key == pygame.K_SPACE:
        # 创建新子弹，加入子弹列表
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


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


def check_events(ai_settings, screen, ship, bullets):
    """
    react on events

    由于按下空格会发射子弹，创建子弹要用到ai_settings, screen, bullets
    因此都作为参数传入
    """
    # handle events in event_list
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            handle_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            handle_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """
    update screen background & elements

    使用ai_settings中的背景颜色，把ship，bullets绘制到screen上
    """
    # draw the background
    screen.fill(ai_settings.bg_color)
    # draw the bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # draw the ship
    ship.blit_me()

    # update display
    pygame.display.flip()
