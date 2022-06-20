import pygame
import sys
from settings import Settings


class SnakeGame():
    """Overall class to manage game assets and behaviors.
    """

    def __init__(self):
        """Initialize the game, and create game resource."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()

        pygame.display.set_caption('Snake Game')

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_key_events()
            self._update_screen()
            pass
    def _check_key_events(self):
        """Response to keypress and mouse events."""
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit(0)

    def _update_screen(self):
        """Update images on the screen."""
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()


if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run_game()
