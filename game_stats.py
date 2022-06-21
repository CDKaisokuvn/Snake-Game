class GameStats:
    """Track statistics for snake game."""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during game."""
        self.score = 0
        self._get_best_score()

    def _get_best_score(self):
        with open('score.txt', 'r') as f:
            self.best_score = int(f.read())
