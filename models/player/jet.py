import pygame
from models.player.vehicle import VehiclePlayer


class JetPlayer(VehiclePlayer):
    def __init__(self, JET_IMAGE: str, sprite_groups: list) -> None:
        super().__init__(JET_IMAGE, sprite_groups)
        self.image = pygame.transform.scale(self.image, (150, 43))
        self.rect = self.image.get_rect()
        self.rect.bottom = self.height // 2
        self.speed_y = 0
        self.y = self.rect.centery
        self.rect.centerx = 100
