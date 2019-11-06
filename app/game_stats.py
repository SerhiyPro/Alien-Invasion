import json
from app.score import Score


class GameStats:
    """Track statistic for Alien Invasion"""

    def __init__(self, game_settings):
        """Initialize statistics"""
        self.game_settings = game_settings

        self.reset_stats()

        # Start game in an inactive way
        self.game_active = False

        # filename = 'best_score.json'
        score = Score()
        self.high_score = score.get_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.game_settings.ship_limit
        self.score = 0
        self.level = 1
