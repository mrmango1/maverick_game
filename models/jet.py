import pygame
from pygame.sprite import Sprite, Group
from models.bullet import Bullet

BULLET_IMAGE = "assets/misil/ecuador.png"

# create jet class
class Jet(Sprite):
    def __init__(self, JET_IMAGE: str, HEIGHT: int) -> None:
        super().__init__()
        self.image_path = JET_IMAGE
        self.image = pygame.image.load(JET_IMAGE)
        self.image = pygame.transform.scale(self.image, (150, 43))
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT // 2
        self.height = HEIGHT
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.isCharge = True


class JetPlayer(Jet):
    def __init__(self, JET_IMAGE: str, HEIGHT: int) -> None:
        super().__init__(JET_IMAGE, HEIGHT)
        self.speed_y = 0
        self.rect.centerx = 100

    def update(self) -> None:
        self.speed_y = 0
        keystate = pygame.key.get_pressed()
        if self.rect.y > 0:
            if keystate[pygame.K_UP]:
                self.speed_y = -5
        if self.rect.y < self.height - 100:
            if keystate[pygame.K_DOWN]:
                self.speed_y = 5
        self.rect.y += self.speed_y

    def shoot(self) -> Bullet:
        self.isCharge = not self.isCharge
        self.image = pygame.image.load(self.haveMisil(self.isCharge))
        self.image = pygame.transform.scale(self.image, (150, 43))
        bullet = Bullet(BULLET_IMAGE, self.rect.centerx, self.rect.centery)
        return bullet

    def haveMisil(self, true) -> str:
        self.jetWithMisil = self.image_path
        self.jetNoMisil = self.image_path.replace("jetWithMisil", "jetNoMisil")
        return self.jetWithMisil if true else self.jetNoMisil


class JetEnemy(Jet):
    def __init__(self, JET_IMAGE: str, HEIGHT: int, WIDTH: int) -> None:
        super().__init__(JET_IMAGE, HEIGHT)
        self.speed_y = 1
        self.rect.centerx = WIDTH - 100
        self.width = WIDTH
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
