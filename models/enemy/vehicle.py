import pygame
from models.bullet import Bullet
from models.model import Vehicle


class VehicleEnemy(Vehicle):
    """Enemy vehicle father class
    Enemy vehicles that operate independient with maching learning or other player
    Args:
        Vehicle (_type_): This class is the father of all enemy vehicle classes
    """

    def __init__(self, JET_IMAGE: str, sprite_groups: list) -> None:
        super().__init__(JET_IMAGE, sprite_groups)
        self.image = pygame.transform.scale(self.image, (150, 43))
        self.rect = self.image.get_rect()
        self.speedy = 3
        self.move = True

    def update(self):
        if self.move:
            self.rect.y += self.speedy
        else:
            self.rect.y -= self.speedy
        if self.rect.top <= 0:
            self.move = True
        if self.rect.bottom >= self.height - 50:
            self.move = False
