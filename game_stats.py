class GameStats:

    def __init__(self, ai_game):
        """Initialize the statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """Initialize the statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
