import math, random, pygame
from model.player.jet import JetPlayer
from model.enemy.jet import JetEnemy
from model.bullet import Bullet
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
    for first, second in hits.items():
        if type(first) != type(second[0]) and type(first) != type(jetPlayer):
            jetEnemy = JetEnemy(JET_WAR, enemy_list)
            enemys.add(jetEnemy)
            all_sprites.add(jetEnemy)
        if type(first) == type(jetPlayer):
            run = False

    all_sprites.draw(screen)
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
