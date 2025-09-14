import pygame

class Paddle:

    def __init__(self, pn_game):
        self.screen = pn_game.screen
        self.settings = pn_game.settings

        right_paddle_l = self.settings.screen_width - self.settings.paddle_width
        paddle_top = self.settings.screen_height // 2 - self.settings.paddle_height // 2
        self.right_paddle = pygame.Rect(right_paddle_l, paddle_top, self.settings.paddle_width,
                                       self.settings.paddle_height)

        self.left_paddle = pygame.Rect(0, paddle_top, self.settings.paddle_width,
                                       self.settings.paddle_height)

    def draw_paddle(self):

        pygame.draw.rect(self.screen, self.settings.paddle_color, self.right_paddle)
        pygame.draw.rect(self.screen, self.settings.paddle_color, self.left_paddle)