# from random import randint


class Settings:

    """Parameters of the game"""

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600

        self.bg_color = (0, 0, 0)
        self.levels = {
            'level1': 0.15,
            'level2': 0.1,
            'level3': 0.08,
            'level4': 0.05,
            'level5': 0.04,
        }

        # Snake segment
        self.segment_width = 20
        self.segment_height = 20
        self.segment_color = (30, 225, 225)
        self.snake_speed = 20

        self.text_color = (230, 10, 230)
