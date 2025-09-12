import sys
import pygame


from settings import Settings

class Pong:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.sreen_width,
                                              self.settings.sreen_height))

        pygame.display.set_caption('Pong')

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


if __name__ == '__main__':
    pn = Pong()
    pn.run_game()
