from pygame import display, image, transform


class Window:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 600

    def __init__(self, caption: str) -> None:
        self.window = 0
        self.blockw = self.SCREEN_WIDTH * (1 / 8)
        self.blockh = self.SCREEN_HEIGHT * (1 / 8)
        self.caption = caption
        self.scroll = 0

    def printboard(self) -> None:
        self.window = display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.window.fill(Window.WHITE)
        display.set_caption(self.caption)
        self.bg = image.load("assets/background/default.jpg").convert()
        self.bg = transform.scale(self.bg, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.bg_rect = self.bg.get_rect()

    def background_move(self) -> None:
        for i in range(2):
            self.window.blit(self.bg, (i * self.SCREEN_WIDTH + self.scroll, 0))
            self.bg_rect.x = i * self.SCREEN_WIDTH + self.scroll
        self.scroll -= 2
        # reset scroll
        if abs(self.scroll) > self.SCREEN_WIDTH:
            self.scroll = 0

    def screen(self) -> display:
        return self.window
