import pygame
from pygame.sprite import Sprite
from pygame.time import get_ticks
from game.window import Window


class Vehicle(Sprite):
    """Principal Vehicle Class Model
    This class is the father or all vehicles classes
    Args:
        Sprite (pygame.sprite.Sprite): This class inherit from Sprite class
    """

    def __init__(self, IMAGE_PATH: str, spriteGroups: list) -> None:
        """Inizilization function
        Inizialize the generic atributtes for a vehicle model
        Args:
            IMAGE_PATH (str): the path of the vehicle image
            spriteGroups (list): All sprites group that this class belongs
        """
        super().__init__()
        self.width, self.height = Window.SCREEN_WIDTH, Window.SCREEN_HEIGHT
        self.imagePath = IMAGE_PATH
        self.spriteGroups = spriteGroups
        self.image = pygame.image.load(IMAGE_PATH)
        self.last = 0
        self.now = get_ticks()
        self.cooldown = 1000
        self.isCharge = True
