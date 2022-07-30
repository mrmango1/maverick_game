import pygame
import random
from pygame.time import get_ticks
from model.bullet import Bullet
from model.object import Vehicle

BULLET_IMAGE = "assets/missile/ecuador.png"


class VehicleEnemy(Vehicle):
    """Enemy vehicle father class
    Enemy vehicles that operate independent with machine learning or other player
    Args:
        model.model.Vehicle (_type_): This class is the father of all enemy vehicle classes
    """

    def __init__(self, jet_image: str, sprite_groups: list) -> None:
        super().__init__(jet_image, sprite_groups)
        self.image = pygame.transform.scale(self.image, (150, 43))
        self.rect = self.image.get_rect()
        self.speedy = 3
        self.move = True
        self.cooldown = random.randint(1000, 2000)

    def update(self):
        self.action()

    def action(self):
        self.now = get_ticks()
        if self.move:
            self.rect.y += self.speedy
        else:
            self.rect.y -= self.speedy
        if self.rect.top <= 0:
            self.move = True
        elif self.rect.bottom >= self.height - 50:
            self.move = False
        if self.now - self.last > self.cooldown:
            if self.rect.top > 0 and self.rect.bottom < self.height - 50:
                self.move = bool(random.getrandbits(1))
            self.last = self.now
            bullet = self.shoot()
            for group in self.spriteGroups:
                group.add(bullet)

    def shoot(self) -> Bullet:
        self.last = self.now
        bullet = Bullet(BULLET_IMAGE, self.rect.centerx, self.rect.centery, False)
        return bullet
