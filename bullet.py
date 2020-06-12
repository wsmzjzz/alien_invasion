import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class for bullet"""

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        # create a bullet at pos:(0, 0)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        # move it to the right place: top of the ship
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # self.y = float(ship.rect.y)

        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    def update(self):
        # self.y -= self.speed
        self.rect.y -= self.speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)