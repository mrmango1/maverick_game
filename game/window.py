from pygame import display, image, transform


class Window:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, width: int, height: int, caption: str) -> None:
        self.sw = width
        self.sh = height
        self.window = 0
        self.blockw = width * (1 / 8)
        self.blockh = height * (1 / 8)
        self.caption = caption
        self.scroll = 0

    def printboard(self) -> None:
        self.window = display.set_mode((self.sw, self.sh))
        self.window.fill(Window.WHITE)
        display.set_caption(self.caption)
        self.bg = image.load("assets/background/default.jpg").convert()
        self.bg = transform.scale(self.bg, (self.sw, self.sh))
        self.bg_rect = self.bg.get_rect()

    def background_move(self) -> None:
        for i in range(2):
            self.window.blit(self.bg, (i * self.sw + self.scroll, 0))
            self.bg_rect.x = i * self.sw + self.scroll
        self.scroll -= 2
        # reset scroll
        if abs(self.scroll) > self.sw:
            self.scroll = 0

    def screen(self) -> display:
        return self.window
