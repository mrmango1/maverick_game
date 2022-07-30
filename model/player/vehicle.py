import pygame
from pygame.time import get_ticks
from model.bullet import Bullet
from model.object import Vehicle

BULLET_IMAGE = "assets/missile/ecuador.png"


class VehiclePlayer(Vehicle):
    def __init__(self, image_path: str, sprite_groups: list) -> None:
        super().__init__(image_path, sprite_groups)
        self.speed_y = 0
        self.jetWithMissile = self.imagePath
        self.jetWithoutMissile = self.imagePath.replace("jetWithMissile", "jetWithoutMissile")

    def update(self) -> None:
        self.now = get_ticks()
        if self.now - self.last <= self.cooldown:
            self.isCharge = False
        else:
            self.isCharge = True
        self.image = pygame.image.load(self.have_missile(self.isCharge))
        self.image = pygame.transform.scale(self.image, (150, 43))
        self.action()

    def action(self) -> None:
        pressed_key = pygame.key.get_pressed()
        # Move up
        if self.rect.y > 0:
            if pressed_key[pygame.K_UP]:
                self.speed_y = -5
        # Move down
        if self.rect.y < self.height - 100:
            if pressed_key[pygame.K_DOWN]:
                self.speed_y = 5
        # Shoot
        if self.isCharge:
            if pressed_key[pygame.K_SPACE]:
                bullet = self.shoot()
                for group in self.spriteGroups:
                    group.add(bullet)
        self.rect.y += self.speed_y
        self.speed_y = 0

    def shoot(self) -> Bullet:
        self.last = self.now
        bullet = Bullet(BULLET_IMAGE, self.rect.centerx, self.rect.centery)
        return bullet

    def have_missile(self, true) -> str:
        return self.jetWithMissile if true else self.jetWithoutMissile
