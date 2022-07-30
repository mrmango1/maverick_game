from model.enemy.vehicle import VehicleEnemy
import random


class JetEnemy(VehicleEnemy):
    def __init__(self, jet_image: str, sprite_groups: list) -> None:
        super().__init__(jet_image, sprite_groups)
        self.rect.centerx = self.width - 100
        self.rect.bottom = random.randint(0, self.height)
