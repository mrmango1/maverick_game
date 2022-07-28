import math, random, pygame
from models.jet import JetPlayer, JetEnemy

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
JET_DEFAULT = "assets/jetWithMisil/default.png"
JET_WAR = "assets/jetWithMisil/war.png"
JET_ECUADOR = "assets/jetWithMisil/ecuador.png"


# Create windows
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maverick")

# Load image
bg = pygame.image.load("assets/background/default.jpg").convert()
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_width = bg.get_width()
bg_rect = bg.get_rect()

# Define variables

scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1


player = pygame.sprite.Group()
enemys = pygame.sprite.Group()
bullets = pygame.sprite.Group()
jetPlayer = JetPlayer(JET_ECUADOR, SCREEN_HEIGHT)
enemy = JetEnemy(JET_WAR, SCREEN_HEIGHT, SCREEN_WIDTH)
player.add(jetPlayer)
enemys.add(enemy)

run = True
while run:

    clock.tick(FPS)

    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
        bg_rect.x = i * bg_width + scroll

    # scroll background
    scroll -= 1
    # reset scroll
    if abs(scroll) > bg_width:
        scroll = 0
    player.update()
    player.draw(screen)
    enemys.update()
    enemys.draw(screen)
    bullets.update()
    bullets.draw(screen)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jetPlayer.shoot(bullets)
    pygame.display.update()

pygame.quit()
