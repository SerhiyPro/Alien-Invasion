from sys import platform


class GameSettings:
    """A class to store all game settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        if platform == "win32":
            import ctypes
            user32 = ctypes.windll.user32
            screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

            self.screen_width = screensize[0]
            self.screen_height = screensize[1] - 100
        elif platform == "darwin" or platform == "linux" or platform == "linux2":
            self.screen_width = 1200
            self.screen_height = 800

        self.bg_color = (230, 230, 230)

        self.ship_limit = 3

        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speed_up_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.time_freeze = 0.5

    def initialize_dynamic_settings(self):
        """Initialize settings that change throught the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.alien_points = 50

        # fleet direction (1 for right, -1 for left)
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale

        self.alien_points = int(self.alien_points * self.score_scale)
