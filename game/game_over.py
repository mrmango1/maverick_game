from pygame_menu import Menu, Theme, events, font
from game.settings import Settings
from pygame import display


class GameOver:
    CAPTION = "GAME OVER"

    def __init__(self, game_screen: display) -> None:
        self.game_screen = game_screen
        self.settings = Settings()
        self.menuTheme = None
        self.create_theme()

    def run_menu(self, run_game) -> None:
        menu = Menu('GAME OVER', 400, 300,
                    theme=self.menuTheme)
        menu.add.text_input('Name :', default='Anderson')
        menu.add.button('Play', run_game)
        menu.add.button('Quit', events.RESET)
        menu.mainloop(self.game_screen)

    def create_theme(self) -> None:
        myFont = font.FONT_MUNRO
        self.menuTheme = Theme(background_color=(0, 0, 0, 0),
                               title_background_color=(4, 47, 126),
                               title_font_shadow=True,
                               widget_padding=25,
                               widget_font=myFont)
