import math, random, pygame
from models.jet import JetPlayer, JetEnemy
from game.window import Window

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
GAME_CAPTION = "Maverick"
JET_DEFAULT = "assets/jetWithMisil/default.png"
JET_WAR = "assets/jetWithMisil/war.png"
JET_ECUADOR = "assets/jetWithMisil/ecuador.png"

# Create windows
window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_CAPTION)
window.printboard()
pygame.display.set_caption("Maverick")
screen = window.screen()

# Instance models and create sprite groups
player = pygame.sprite.Group()
enemys = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
jetPlayer = JetPlayer(JET_ECUADOR, SCREEN_HEIGHT)
jetEnemy = JetEnemy(JET_WAR, SCREEN_HEIGHT, SCREEN_WIDTH)
player.add(jetPlayer)
enemys.add(jetEnemy)
all_sprites.add(jetPlayer)
all_sprites.add(enemys)

run = True
while run:
    clock.tick(FPS)
    window.background_move()

    all_sprites.update()
    hits = pygame.sprite.groupcollide(player, enemys, True, True)
    if hits:
        testene = JetEnemy(JET_WAR, SCREEN_HEIGHT, SCREEN_WIDTH)
        enemys.add(testene)
        all_sprites.add(testene)

    all_sprites.draw(screen)
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = jetPlayer.shoot()
                all_sprites.add(bullet)
                player.add(bullet)
    pygame.display.update()

pygame.quit()
