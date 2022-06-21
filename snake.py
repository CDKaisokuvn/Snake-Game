from pygame.sprite import Sprite
import pygame


class Snake(Sprite):

    """Snake class"""

    def __init__(self, snake_game):
        super().__init__()
        self.settings = snake_game.settings
        self.screen = snake_game.screen
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(
            0, 0, self.settings.segment_width, self.settings.segment_height)

        self.reset_movement_state()

    def first_segment(self):
        """Put the first segment at the center of the screen"""
        self.rect.center = self.screen_rect.center

    def draw_segments(self):
        """Display segments on the screen
        """
        pygame.draw.rect(self.screen, self.settings.segment_color, self.rect)

    def reset_movement_state(self):
        """Initialize movement states"""
        self.moving_right = False
        self.moving_up = False
        self.moving_left = False
        self.moving_down = False

    def move(self):
        """Move first segment"""
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom - 10:
            self.y += self.settings.snake_speed

        if self.moving_left and self.rect.left > 10:

            self.x -= self.settings.snake_speed
        if self.moving_up and self.rect.top > 10:

            self.y -= self.settings.snake_speed
        if self.moving_right and self.rect.right < self.screen_rect.right - 10:

            self.x += self.settings.snake_speed

        self.rect.centerx = self.x
        self.rect.centery = self.y
