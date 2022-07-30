from pygame.sprite import Sprite
from pygame import image, transform


class Bullet(Sprite):
    def __init__(
            self, bullet_image: str, x: int, y: int, direction: bool = True
    ) -> None:
        super().__init__()
        self.image = image.load(bullet_image)
        self.image = transform.scale(self.image, (50, 13))
        self.rect = self.image.get_rect()
        self.rect.y = y + 5
        self.rect.centerx = x
        self.speed_x = 8
        self.direction = direction

    def update(self) -> None:
        if self.direction:
            self.rect.x += self.speed_x
            if self.rect.right > 1200:
                self.kill()
        else:
            self.rect.x -= self.speed_x
            if self.rect.right <= 0:
                self.kill()
