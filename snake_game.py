import pygame
import sys
from time import sleep
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
            # Move the last segments before the first one
            self._update_snake_movement()
            # Use sleep to control the movements of each segment
            sleep(0.07)
            # Move the first segment
            self.first_segment.move()
            self._update_screen()

    def _check_key_events(self):
        """Response to keypress and mouse events."""
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                if event.key == pygame.K_DOWN and not self.first_segment.moving_up:
                    self.first_segment.reset_movement_state()
                    self.first_segment.moving_down = True

                elif event.key == pygame.K_UP and not self.first_segment.moving_down:
                    self.first_segment.reset_movement_state()
                    self.first_segment.moving_up = True

                elif event.key == pygame.K_LEFT and not self.first_segment.moving_right:
                    self.first_segment.reset_movement_state()
                    self.first_segment.moving_left = True

                elif event.key == pygame.K_RIGHT and not self.first_segment.moving_left:
                    self.first_segment.reset_movement_state()
                    self.first_segment.moving_right = True

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

    def _update_snake_movement(self):

        segments = self.snake.sprites()
        segments.reverse()
        
        for i in range(len(segments)):
            if i < len(segments) - 1:
                segments[i].rect.centerx = segments[i+1].rect.centerx
                segments[i].rect.centery = segments[i+1].rect.centery

    def _update_screen(self):
        """Update images on the screen."""
        self.screen.fill(self.settings.bg_color)
        for segment in self.snake.sprites():
            segment.draw_segments()

        pygame.display.flip()


if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run_game()
