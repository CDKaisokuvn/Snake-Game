import pygame
from pygame.sprite import Sprite


class Food(Sprite):
    """Food class"""

    def __init__(self, snake_game):
        super().__init__()
        self.settings = snake_game.settings
        self.screen = snake_game.screen
        self.screen_rect = self.screen.get_rect()
        self.is_exist = False
        self.x = 0
        self.y = 0

    def draw_food(self):
        self.rect = pygame.draw.circle(
            self.screen, (255, 255, 255), (self.x, self.y), 10)
        self.is_exist = True
