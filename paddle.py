import pygame
from pygame.sprite import Sprite

class Paddle(Sprite):

    def __init__(self, pn_game, left, top):
        super().__init__()
        self.screen = pn_game.screen
        self.settings = pn_game.settings

        self.image = pygame.Surface([self.settings.paddle_width,
                                     self.settings.paddle_height])
        self.image.fill(self.settings.paddle_color)
        self.rect = self.image.get_rect()

        self.rect.x = left
        self.rect.y = top

        self.x = left
        self.y = top

        self.move_up_l = False
        self.move_down_l = False

        self.move_up_r = False
        self.move_down_r = False

    def _check_bounds(self):
        if self.y < self.settings.bounds_paddle_top:
            self.y = self.settings.bounds_paddle_top
        elif self.y > self.settings.bounds_paddle_bottm:
            self.y = self.settings.bounds_paddle_bottm

    def _move_left(self):
        if self.move_up_l:
            self.y -= self.settings.speed_paddle
        if self.move_down_l:
            self.y += self.settings.speed_paddle

    def _move_right(self):
        if self.move_up_r:
            self.y -= self.settings.speed_paddle
        if self.move_down_r:
            self.y += self.settings.speed_paddle

    def update(self):
        self._move_left()
        self._move_right()

        self._check_bounds()

        self.rect.y = int(self.y)

