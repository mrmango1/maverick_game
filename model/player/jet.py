import pygame
from model.player.vehicle import VehiclePlayer


class JetPlayer(VehiclePlayer):
    def __init__(self, jet_image: str, sprite_groups: list) -> None:
        super().__init__(jet_image, sprite_groups)
        self.image = pygame.transform.scale(self.image, (150, 43))
        self.rect = self.image.get_rect()
        self.rect.bottom = self.height // 2
        self.speed_y = 0
        self.y = self.rect.centery
        self.rect.centerx = 100
