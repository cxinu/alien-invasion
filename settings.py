class Settings:
    """This class stores all the settings for the alien invasion"""

    def __init__(self):
        """------------Iniitalize the game settings-------"""
        """----------------Screen Settings-------------------"""
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (25, 23, 33)
        self.ship_speed = 1.5
        self.ship_limit = 3
        """Bullet settings"""
        self.bullet_speed = 3.0
        self.bullet_width = 3.0
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.alien_speed = 1.0
        # Fleet direction of +1 represents right; -1 represents left
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase the speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
