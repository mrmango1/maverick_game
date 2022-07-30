import math, random, pygame
from models.player.jet import JetPlayer
from models.enemy.jet import JetEnemy
from game.window import Window
from time import sleep

pygame.init()

clock = pygame.time.Clock()
FPS = 60

GAME_CAPTION = "Maverick"
JET_DEFAULT = "assets/jetWithMisil/default.png"
JET_WAR = "assets/jetWithMisil/war.png"
JET_ECUADOR = "assets/jetWithMisil/ecuador.png"

# Create windows
window = Window(GAME_CAPTION)
window.printboard()
pygame.display.set_caption("Maverick")
screen = window.screen()

# Instance models and create sprite groups
player = pygame.sprite.Group()
enemys = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player_list = [player, all_sprites]
enemy_list = [enemys, all_sprites]
jetPlayer = JetPlayer(JET_ECUADOR, player_list)
jetEnemy = JetEnemy(JET_WAR, enemy_list)

player.add(jetPlayer)
enemys.add(jetEnemy)

all_sprites.add(player)
all_sprites.add(enemys)

run = True
while run:
    clock.tick(FPS)
    window.background_move()

    all_sprites.update()
    hits = pygame.sprite.groupcollide(player, enemys, True, True)
    if hits:
        jetEnemy = JetEnemy(JET_WAR, enemy_list)
        enemys.add(jetEnemy)
        all_sprites.add(jetEnemy)

    all_sprites.draw(screen)
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
