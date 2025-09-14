import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):

    def __init__(self, pn_game):
        super().__init__()
        self.screen = pn_game.screen
        self.settings = pn_game.settings

        self.image = pygame.Surface([self.settings.ball_size,
                                     self.settings.ball_size])
        self.image.set_colorkey('black')
        pygame.draw.circle(self.image, self.settings.ball_color,
                           (self.settings.ball_size // 2,
                            self.settings.ball_size // 2),
                            self.settings.ball_size // 2)

        self.rect = self.image.get_rect()

        self.y = self.settings.screen_height // 2
        self.x = self.settings.screen_width // 2 - self.settings.net_width


        position = randint(1, 2)

        if position == 2:
            self.x += 100
        elif position == 1:
            self.x -= 100


        self.rect.y = int(self.y)
        self.rect.x = int(self.x)

    def _check_bounds(self):

        if (self.y >= self.settings.screen_height - self.settings.border_height -
                                                        self.settings.ball_size):
            self.settings.ball_dy *= -1
            self.settings.ball_speed_y *= self.settings.ball_dy


        elif self.y <= self.settings.border_height:
            self.settings.ball_dy *= -1
            self.settings.ball_speed_y *= self.settings.ball_dy


    def _check_paddle(self):

        if (self.x >= (self.settings.screen_width - self.settings.paddle_width - self.settings.ball_size)
                and self.x >= self.settings.paddle_width):
            self.settings.ball_dx *= -1
            self.settings.ball_speed_x *= self.settings.ball_dx
            self.settings.ball_dy *= -1
            self.settings.ball_speed_y *= self.settings.ball_dy

        elif self.x <= self.settings.paddle_width:
            self.settings.ball_dx *= -1
            self.settings.ball_speed_x *= self.settings.ball_dx
            self.settings.ball_dy *= -1
            self.settings.ball_speed_y *= self.settings.ball_dy

    def update(self):
        self._check_bounds()
        self._check_paddle()
        self.y += self.settings.ball_speed_y
        self.x += self.settings.ball_speed_x




        self.rect.y = int(self.y)
        self.rect.x = int(self.x)