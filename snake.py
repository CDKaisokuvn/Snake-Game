from pygame.sprite import Sprite
import pygame


class Snake(Sprite):

    """Snake"""

    def __init__(self, snake_game):
        super().__init__()
        self.settings = snake_game.settings
        self.screen = snake_game.screen
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(
            0, 0, self.settings.segment_width, self.settings.segment_height)

    def first_segment(self):
        """Put the first segment at the center of the screen"""
        self.rect.center = self.screen_rect.center

    def draw_segments(self):
        """Display segments on the screen
        """
        pygame.draw.rect(self.screen, self.settings.segment_color, self.rect)
