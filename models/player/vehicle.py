import pygame
from pygame.time import get_ticks
from models.bullet import Bullet
from models.model import Vehicle

BULLET_IMAGE = "assets/misil/ecuador.png"


class VehiclePlayer(Vehicle):
    def __init__(self, IMAGE_PATH: str, spriteGroups: list) -> None:
        super().__init__(IMAGE_PATH, spriteGroups)

    def update(self) -> None:
        self.now = get_ticks()
        if self.now - self.last <= self.cooldown:
            self.isCharge = False
        else:
            self.isCharge = True
        self.image = pygame.image.load(self.have_misil(self.isCharge))
        self.image = pygame.transform.scale(self.image, (150, 43))
        self.speed_y = 0
        self.action()

    def action(self) -> None:
        keystate = pygame.key.get_pressed()
        # Move up
        if self.rect.y > 0:
            if keystate[pygame.K_UP]:
                self.speed_y = -5
        # Move down
        if self.rect.y < self.height - 100:
            if keystate[pygame.K_DOWN]:
                self.speed_y = 5
        # Shoot
        if self.isCharge:
            if keystate[pygame.K_SPACE]:
                bullet = self.shoot()
                for group in self.sprite_groups:
                    group.add(bullet)
        self.rect.y += self.speed_y

    def shoot(self) -> Bullet:
        self.last = self.now
        bullet = Bullet(BULLET_IMAGE, self.rect.centerx, self.rect.centery)
        return bullet

    def have_misil(self, true) -> str:
        self.jetWithMisil = self.image_path
        self.jetNoMisil = self.image_path.replace("jetWithMisil", "jetNoMisil")
        return self.jetWithMisil if true else self.jetNoMisil
