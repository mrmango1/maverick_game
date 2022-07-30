import pygame
import random
from pygame.time import get_ticks
from pygame.sprite import Sprite, Group
from models.bullet import Bullet

BULLET_IMAGE = "assets/misil/ecuador.png"

# create jet class
class Jet(Sprite):
    def __init__(self, JET_IMAGE: str, HEIGHT: int, sprite_groups: list) -> None:
        super().__init__()
        self.image_path = JET_IMAGE
        self.sprite_groups = sprite_groups
        self.image = pygame.image.load(JET_IMAGE)
        self.image = pygame.transform.scale(self.image, (150, 43))
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT // 2
        self.height = HEIGHT
        self.y = self.rect.centery
        self.last = 0
        self.now = get_ticks()
        self.cooldown = 1000
        self.isCharge = True


class JetPlayer(Jet):
    def __init__(self, JET_IMAGE: str, HEIGHT: int, sprite_groups: list) -> None:
        super().__init__(JET_IMAGE, HEIGHT, sprite_groups)
        self.speed_y = 0
        self.rect.centerx = 100

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


class JetEnemy(Jet):
    def __init__(self, JET_IMAGE: str, size: list, sprite_groups: list) -> None:
        super().__init__(JET_IMAGE, size[1], sprite_groups)
        self.rect.centerx = size[0] - 100
        self.speedy = 3
        self.move = True
        self.rect.bottom = random.randint(0, self.height)

    def update(self):
        if self.move:
            self.rect.y += self.speedy
        else:
            self.rect.y -= self.speedy
        if self.rect.top <= 0:
            self.move = True
        if self.rect.bottom >= self.height - 50:
            self.move = False
