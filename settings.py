"""A class that restore all settings"""


class Settings:

    def __init__(self):
        """init all settings"""
        # about screen
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (0, 0, 0)
        # about the ship
        self.ship_speed = 5.5
        # about bullets
        self.bullet_speed = 7.6
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 160, 160, 30
