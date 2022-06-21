class GameStats:
    """Track statistics for snake game."""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.game_active = False
        self.reset_stats()
        self._get_best_score()

    def reset_stats(self):
        """Initialize statistics that can change during game."""
        self.score = 0
        self.level = 1

    def _get_best_score(self):
        with open('score.txt', 'r') as f:
            self.best_score = int(f.read())

    def _update_best_score(self):
        if self.score > self.best_score:
            with open('score.txt', 'w') as f:
                self.best_score = self.score
                f.write(str(self.best_score))
