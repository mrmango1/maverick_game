import random
from pygame import font


class Settings:
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
        """
        This function takes a string as an argument and returns a string

        :param jet: The name of the jet you want to use
        :type jet: str
        :return: The jetDefault string is being returned.
        """
        return self.jetDefault.replace("default", jet)

    def get_aleatory_jet(self) -> str:
        """
        It returns a random jet from a list of jet variants
        :return: The method is returning the jetDefault string, but replacing the word "default" with the randomJet string.
        """

        self.randomJet = random.choice(self.jetVariants)
        return self.jetDefault.replace("default", self.randomJet)

    def get_font(self, size: int):
        return font.Font("assets/font/PixeloidMono.ttf", size)
