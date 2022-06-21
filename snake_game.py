import pygame
import sys
from settings import Settings
from snake import Snake


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
        self.snake = pygame.sprite.Group()

        pygame.display.set_caption('Snake Game')

        self._initialize_snake()

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

    def _initialize_snake(self):
        """Create 3 segments for the snake and"""
        for i in range(3):
            if i == 0:
                self.first_segment = Snake(self)
                self.first_segment.first_segment()
                self.snake.add(self.first_segment)
            else:
                segment = Snake(self)
                self.snake.add(segment)
        for i in range(3):
            if i != 0:
                self.snake.sprites()[i].rect.x = self.snake.sprites()[
                    i-1].rect.x - self.settings.segment_width
                self.snake.sprites()[i].rect.y = self.snake.sprites()[
                    i-1].rect.y

    def _update_screen(self):
        """Update images on the screen."""
        self.screen.fill(self.settings.bg_color)
        for segment in self.snake.sprites():
            segment.draw_segments()

        pygame.display.flip()


if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run_game()
