import pygame
from pygame.sprite import Group, groupcollide
from model.player.jet import JetPlayer
from model.enemy.jet import JetEnemy
from game.window import Window

pygame.init()

clock = pygame.time.Clock()
FPS = 60

GAME_CAPTION = "Maverick"
JET_DEFAULT = "assets/jetWithMissile/default.png"
JET_WAR = "assets/jetWithMissile/war.png"
JET_ECUADOR = "assets/jetWithMissile/ecuador.png"

# Create windows
window = Window(GAME_CAPTION)
window.printboard()
pygame.display.set_caption("Maverick")
screen = window.screen()

# Instance models and create sprite groups
player = Group()
enemies = Group()
all_sprites = Group()

player_list = [player, all_sprites]
enemy_list = [enemies, all_sprites]

jetPlayer = JetPlayer(JET_ECUADOR, player_list)
jetEnemy = JetEnemy(JET_WAR, enemy_list)

player.add(jetPlayer)
enemies.add(jetEnemy)

all_sprites.add(player)
all_sprites.add(enemies)

run = True
while run:
    clock.tick(FPS)
    window.background_move()

    all_sprites.update()
    hits = groupcollide(player, enemies, True, True)
    for first, second in hits.items():
        if not isinstance(first, type(second[0])) and not isinstance(first, type(jetPlayer)):
            jetEnemy = JetEnemy(JET_WAR, enemy_list)
            enemies.add(jetEnemy)
            all_sprites.add(jetEnemy)
        if isinstance(first, type(jetPlayer)):
            run = False

    all_sprites.draw(screen)
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
