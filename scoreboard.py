import pygame


class ScoreBoard:
    """ScoreBoard class"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.game_stats = ai_game.game_stats

        self.font = pygame.font.SysFont(None, 36)
        self.prep_scoreboard()
        self.prep_best_score()

    def prep_scoreboard(self):
        """Turn score into a rendered image."""
        # Score on the top-left
        score = (self.game_stats.score)
        score_str = str(score)
        self.score_img = self.font.render(
            score_str, True, self.settings.text_color, self.settings.bg_color)
        self.score_img_rect = self.score_img.get_rect()
        self.score_img_rect.right = self.screen_rect.right
        self.score_img_rect.top = 5

    def prep_best_score(self):
        self.best_score = self.game_stats.best_score
        best_score_str = str(f'Best scores: {self.best_score} ')
        self.best_score_img = self.font.render(
            best_score_str, True, self.settings.text_color)
        self.best_score_img_rect = self.best_score_img.get_rect()

        self.best_score_img_rect.top = 5
        self.best_score_img_rect.left = self.screen_rect.left

    def draw_score(self):
        """Draw score on the screen"""
        self.screen.blit(self.score_img, self.score_img_rect)
        self.screen.blit(self.best_score_img, self.best_score_img_rect)
