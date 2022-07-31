from pygame import display, image, transform


class Menu:
    CAPTION = "Menu"

    def __init__(self, caption: str) -> None:
        self.window = 0
        self.blockw = self.SCREEN_WIDTH * (1 / 8)
        self.blockh = self.SCREEN_HEIGHT * (1 / 8)
        self.caption = caption
        self.scroll = 0