import pygame

JET_DEFAULT = "assets/jetWithMisil/default.png"

# create jet class
class Jet(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(JET_DEFAULT)
        self.rect = self.image.get_rect()

    # class Jet(pygame.sprite.Sprite):
    #     def __init__(self, x: int, y: int, health: int) -> None:
    #         super().__init__()
    #         self.image = pygame.image.load(JET_DEFAULT)
    #         self.rect = self.image.get_rect()
    #         self.rect.center = (x, y)
    #         self.health_start = health
    #         self.health_remaining = health
    #         self.last_shot = pygame.time.get_ticks()

    def update(self, screen_width) -> int:
        # set movement speed
        speed = 8
        # set cooldown variable
        cooldown = 500  # miliseconds
        game_over = 0
