
class Game_Stats:

    def __init__(self, pn_game):

        self.settings = pn_game.settings
        self._reset_game()




    def _reset_game(self):
        self.p1_score = 0
        self.p2_score = 0

