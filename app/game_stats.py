class GameStats:
    """Track statistick for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.game_active = True

        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
