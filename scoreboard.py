import pygame


class Scoreboard:

    def __init__(self, pn_game):
        self.pn_game = pn_game
        self.screen = pn_game.screen
        self.settings = pn_game.settings
        self.screen_rect = self.screen.get_rect()
        self.stats = pn_game.stats

        self.text_color = (255, 255, 255)
        self.winner_color = (128, 255, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_p1_score()
        self.prep_p2_score()

    def prep_p1_score(self):
        p1_score_str = str(self.stats.p1_score)
        self.p1_image = self.font.render(p1_score_str, True,
                                         self.text_color, self.settings.bg_color)

        self.p1_score_rect = self.p1_image.get_rect()
        self.p1_score_rect.left = self.screen_rect.left + 500
        self.p1_score_rect.top = 60

    def prep_p2_score(self):
        p2_score_str = str(self.stats.p2_score)
        self.p2_image = self.font.render(p2_score_str, True,
                                         self.text_color, self.settings.bg_color)

        self.p2_score_rect = self.p2_image.get_rect()
        self.p2_score_rect.right = self.screen_rect.right - 500
        self.p2_score_rect.top = 60

    def prep_winner(self, winner):
        message = f"Congrats! {winner}"

        self.winner_image = self.font.render(message, True,
                                             self.winner_color, self.settings.bg_color)

        self.winner_rect = self.winner_image.get_rect()
        self.winner_rect.right = self.settings.screen_width // 2 + self.winner_rect.width // 2
        self.winner_rect.top = self.settings.screen_height // 2

    def show_winner(self):
        self.screen.blit(self.winner_image, self.winner_rect)

    def show_score(self):
        self.screen.blit(self.p1_image, self.p1_score_rect)
        self.screen.blit(self.p2_image, self.p2_score_rect)
