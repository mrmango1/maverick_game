from pygame_menu import Theme, Menu, events, font
from pygame import display

import game.game
from game.settings import Settings


class GameMenu:
    CAPTION = "Menu"

    def __init__(self, game_screen: display) -> None:
        self.game_screen = game_screen
        self.settings = Settings()
        self.menuTheme = None
        self.create_theme()

    def run_menu(self, maverick: game.game.Maverick) -> None:
        menu = Menu('Bienvenido', 400, 300,
                    theme=self.menuTheme)
        menu.add.text_input('Name :', default='Anderson')
        menu.add.button('Play', maverick)
        menu.add.button('Quit', events.EXIT)
        menu.mainloop(self.game_screen)

    def create_theme(self) -> None:
        myFont = font.FONT_MUNRO
        self.menuTheme = Theme(background_color=(0, 0, 0, 0),
                               title_background_color=(4, 47, 126),
                               title_font_shadow=True,
                               widget_padding=25,
                               widget_font=myFont)
