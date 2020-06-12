"""A class for the player-controlled ship"""
import pygame


class Ship:
    def __init__(self, screen):
        """initialize the ship & its position"""
        # draw on the main screen
        self.screen = screen
        # load the image
        self.image = pygame.image.load('images/ship.bmp')
        # get the rect outside the ship
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # make it at center bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blit_me(self):
        """draw the ship"""
        self.screen.blit(self.image, self.rect)
