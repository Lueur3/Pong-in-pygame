
class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800

        self.border_width = self.screen_width
        self.border_height = 20
        self.border_color = 'white'

        self.net_width = 15
        self.net_height = self.screen_height

        self.paddle_width = 25
        self.paddle_height = 300
        self.paddle_color = 'blue'

        self.game_active = False