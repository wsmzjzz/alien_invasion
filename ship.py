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
        # 为了方便使用浮点数速度计算位移量
        self.x_center = float(self.rect.centerx)
        # sign of moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self, ai_settings):
        """update moved position"""
        # move ship right & keep it in screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x_center += ai_settings.ship_speed
        # move ship left & keep it in screen
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x_center -= ai_settings.ship_speed
        # move ship up
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= ai_settings.ship_speed
        # move ship down
        # 'centery < bottom' 保证飞船下半部分可以隐到窗口下方
        if self.moving_down and self.rect.centery < self.screen_rect.bottom:
            self.rect.y += ai_settings.ship_speed
        # 最终决定ship位置的还是rect.centerx参数
        self.rect.centerx = self.x_center

    def blit_me(self):
        """draw the ship"""
        self.screen.blit(self.image, self.rect)
