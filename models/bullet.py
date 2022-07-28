import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, BULLET_IMAGE: str, x: int, y: int) -> None:
        super().__init__()
        self.image = pygame.image.load(BULLET_IMAGE)
        self.image = pygame.transform.scale(self.image, (50, 13))
        self.rect = self.image.get_rect()
        self.rect.y = y + 5
        self.rect.centerx = x
        self.speedx = 8

    def update(self) -> None:
        self.rect.x += self.speedx
        if self.rect.right > 1200:
            self.kill()
