from turtle import width


class Settings:

    """Parameters of the game"""

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600

        self.bg_color = (0, 0, 0)

        # Snake segment
        self.segment_width = 20
        self.segment_height = 20
        self.segment_color = (255, 255, 255)
        self.snake_speed = 20

        self.text_color = (230, 230, 230)
