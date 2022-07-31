import pygame
from pygame.sprite import Sprite
from pygame.time import get_ticks
from game.settings import Settings


class Vehicle(Sprite):
    """Principal Vehicle Class Model
    This class is the father or all vehicles classes
    Args:
        pygame.sprite.Sprite (_type_): This class inherit from Sprite class
    """

    def __init__(self, image_path: str, sprite_groups: list) -> None:
        """Initialization function
        Initialize the generic attributes for a vehicle model
        Args:
            image_path (str): the path of the vehicle image
            sprite_groups (list): All sprites group that this class belongs
        """
        super().__init__()
        self.width, self.height = Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT
        self.imagePath = image_path
        self.spriteGroups = sprite_groups
        self.image = pygame.image.load(image_path)
        self.last = 0
        self.now = get_ticks()
        self.cooldown = 1000
        self.isCharge = True
