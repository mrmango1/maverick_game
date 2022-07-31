import random


class Settings:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 600
    FPS = 60

    def __init__(self) -> None:
        self.jetDefault = "assets/jetWithMissile/default.png"
        self.jetVariants = ["default", "war", "ecuador"]
        self.randomJet = None
        self.gameCaption = "Maverick"
        self.backgroundImage = "assets/background/default.jpg"

        self.window = 0
        self.scroll = 0
        self.background = None
        self.background_rect = None

    def get_jet(self, jet: str) -> str:
        return self.jetDefault.replace("default", jet)

    def get_aleatory_jet(self) -> str:
        self.randomJet = random.choice(self.jetVariants)
        return self.jetDefault.replace("default", self.randomJet)
