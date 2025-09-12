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

    @staticmethod
    def quit_game():
        pygame.quit()
        sys.exit()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Pong.quit_game()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    Pong.quit_game()

    

    def run_game(self):

        while True:
            self._check_events()


            pygame.display.flip()



if __name__ == '__main__':
    pn = Pong()
    pn.run_game()
