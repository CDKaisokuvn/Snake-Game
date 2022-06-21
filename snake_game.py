import pygame
import sys
from time import sleep
from random import randint

from settings import Settings
from snake import Snake
from food import Food
from game_stats import GameStats
from scoreboard import ScoreBoard


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
        self.food = Food(self)
        self.game_stats = GameStats(self)
        self.score_board = ScoreBoard(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_key_events()
            if self.game_stats.game_active:

                # Move the last segments before the first one
                self._update_snake_movement()
            # Use sleep to control the movements of each segment
                sleep(0.07)
            # Move the first segment
                self.first_segment.move()
                self._game_over()
                self.score_board.prep_scoreboard()
                self.score_board.prep_best_score()
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
                    self.game_stats.game_active = True

                elif event.key == pygame.K_UP and not self.first_segment.moving_down:
                    self.first_segment.reset_movement_state()
                    self.first_segment.moving_up = True
                    self.game_stats.game_active = True

                elif event.key == pygame.K_LEFT and not self.first_segment.moving_right:
                    self.first_segment.reset_movement_state()
                    self.first_segment.moving_left = True
                    self.game_stats.game_active = True

                elif event.key == pygame.K_RIGHT and not self.first_segment.moving_left:
                    self.first_segment.reset_movement_state()
                    self.first_segment.moving_right = True
                    self.game_stats.game_active = True

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
        """Moving the snake"""
        segments = self.snake.sprites()
        segments.reverse()

        for i in range(len(segments)):
            if i < len(segments) - 1:
                segment_centerx = segments[i+1].rect.centerx
                segment_centery = segments[i+1].rect.centery
                segments[i].rect.centerx = segment_centerx
                segments[i].rect.centery = segment_centery

    def _update_food(self):
        """Random a position for food"""
        if not self.food.is_exist:
            self.food.x = randint(10, self.screen_rect.width - 10)
            self.food.y = randint(10, self.screen_rect.height - 10)
        self.food.draw_food()

    def _update_screen(self):
        """Update images on the screen."""
        self.screen.fill(self.settings.bg_color)
        for segment in self.snake.sprites():
            segment.draw_segments()
        self._update_food()
        self._eat_food()
        self.score_board.draw_score()
        # pygame.display.update()
        pygame.display.flip()

    def _update_score(self):
        self.game_stats.score += 1
        print(self.game_stats.score)

    def _eat_food(self):
        """Detect collision between the first segment and food"""
        has_collision = pygame.sprite.collide_rect(
            self.food, self.first_segment)

        if has_collision:
            # Reset food position.
            self.food.is_exist = False

            # Add a new segment to the snake.
            segment = Snake(self)
            segment1_centerx = self.first_segment.rect.centerx
            segment1_centery = self.first_segment.rect.centery
            segment.rect.centerx = segment1_centerx
            segment.rect.centery = segment1_centery
            self.snake.add(segment)

            # Update Score
            self._update_score()

    # TODO: Game over
    def _game_over(self):
        # Collision with the border
        has_collision_borders = self._has_collision_borders()

        # Collision with the segments

        has_collision_segments = self._has_collision_segments()

        # TODO: Game over
        if has_collision_borders or has_collision_segments:
            self.game_stats.game_active = False
            self.game_stats._update_best_score()
            self.snake.empty()
            self._initialize_snake()
            self.game_stats.reset_stats()
            self._update_food()

    def _has_collision_borders(self):
        """Detect the collision between the first segment and the border"""
        if self.first_segment.rect.centerx <= 10 or self.first_segment.rect.centery <= 10 or self.first_segment.rect.centerx >= self.screen_rect.right-10 or self.first_segment.rect.centery >= self.screen_rect.bottom - 10:
            return True

        return False

    def _has_collision_segments(self):
        segments = self.snake.copy().sprites()
        segments.remove(self.first_segment)
        if pygame.sprite.spritecollideany(self.first_segment, segments):
            return True
        return False


if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run_game()
