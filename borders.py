import pygame

class Borders:

    def __init__(self, pn_game):
        self.screen = pn_game.screen
        self.settings = pn_game.settings

        self.top_border = pygame.Rect(0, 0, self.settings.border_width,
                                      self.settings.border_height)
        bot_pos = self.settings.screen_height - self.settings.border_height
        self.bottom_border = pygame.Rect(0, bot_pos, self.settings.border_width,
                                      self.settings.border_height)

        net_pos_left = self.settings.screen_width // 2 - self.settings.net_width // 2

        self.net = pygame.Rect(net_pos_left, 0, self.settings.net_width,
                               self.settings.net_height)



    def draw(self):
        pygame.draw.rect(self.screen, 'white', self.top_border)
        pygame.draw.rect(self.screen, 'white', self.bottom_border)
        pygame.draw.rect(self.screen, 'white', self.net)