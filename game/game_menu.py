from pygame_menu import Theme, Menu, events, font
from pygame import display, event, QUIT
from game.game import Maverick
from game.settings import Settings


class GameMenu:
    CAPTION = "Menu"

    def __init__(self, game_screen: display) -> None:
        self.game_screen = game_screen
        self.settings = Settings()
        self.game = Maverick()
        self.menuTheme = None
        self.menu = None

    def run_menu(self) -> None:
        self.create_theme()
        while True:
            events = event.get()
            for e in events:
                if e.type == QUIT:
                    exit()

            if self.menu.is_enabled():
                self.menu.update(events)
                self.menu.draw(self.game_screen)

            display.update()

    def create_theme(self) -> None:
        myFont = font.FONT_MUNRO
        self.menuTheme = Theme(background_color=(0, 0, 0, 0),
                               title_background_color=(4, 47, 126),
                               title_font_shadow=True,
                               widget_padding=25,
                               widget_font=myFont)
        self.menu = Menu('Bienvenido', 400, 300,
                    theme=self.menuTheme)
        self.menu.add.text_input('Name :', default='Anderson')
        self.menu.add.button('Play', self.game.run_game)
        self.menu.add.button('Quit', events.EXIT)
        self.menu.mainloop(self.game_screen)