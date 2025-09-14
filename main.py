import sys
import pygame


from settings import Settings
from borders import Borders
from paddle import  Paddle
from ball import Ball

class Pong:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                              self.settings.screen_height))

        self.screen.fill(self.settings.bg_color)
        pygame.display.set_caption('Pong')

        self.bords = Borders(self)

        self.r_paddle = Paddle(self, *self.settings.l_pos)
        self.l_paddle = Paddle(self, *self.settings.r_pos)

        self.paddleGroup = pygame.sprite.Group()
        self.paddleGroup.add(self.r_paddle, self.l_paddle)

        self.ball = Ball(self)
        self.ballGroup = pygame.sprite.Group()
        self.ballGroup.add(self.ball)

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

                self._keyDown_events(event)

            elif event.type == pygame.KEYUP:
                self._keyUp_events(event)

    def _keyDown_events(self, event):
        if event.key == pygame.K_UP:
            self.r_paddle.move_up_r = True
        elif event.key == pygame.K_DOWN:
            self.r_paddle.move_down_r = True

        if event.key == pygame.K_w:
            self.l_paddle.move_up_l = True
        elif event.key == pygame.K_s:
            self.l_paddle.move_down_l = True

    def _keyUp_events(self, event):
        if event.key == pygame.K_UP:
            self.r_paddle.move_up_r = False
        elif event.key == pygame.K_DOWN:
            self.r_paddle.move_down_r = False

        if event.key == pygame.K_w:
            self.l_paddle.move_up_l = False
        elif event.key == pygame.K_s:
            self.l_paddle.move_down_l = False



    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.bords.draw_borders()

        self.paddleGroup.draw(self.screen)
        self.ballGroup.draw(self.screen)


        pygame.display.flip()



    def run_game(self):

        while True:
            self._check_events()
            self.paddleGroup.update()
            self.ballGroup.update()




            self._update_screen()








if __name__ == '__main__':
    pn = Pong()
    pn.run_game()
