import pygame
from pygame.sprite import Sprite

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

        self.rect.y = 600
        self.rect.x = 250


