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


    def update(self):
        if self.move_up_r:
            self.y -= 1
        if self.move_down_r:
            self.y += 1

        self.rect.y = self.y

