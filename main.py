import pygame
import math
from models.jet import Jet

pygame.init()

clock = pygame.time.Clock()
FPS = 60
# Define colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

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


jet = pygame.image.load("assets/jetWithMisil/default.png")
jet = pygame.transform.scale(jet, (150, 43))

run = True
while run:

    clock.tick(FPS)

    # draw scrolling background
    for i in range(0, 2):
        screen.blit(bg, (i * bg_width + scroll, 0))
        bg_rect.x = i * bg_width + scroll
        pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)

    # scroll background
    scroll -= 3
    # reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    # mouse_pos = pygame.mouse.get_pos()
    # x, y = mouse_pos[0], mouse_pos[1]
    # # set bg
    # screen.fill(WHITE)
    # ### Drawing zone
    # pygame.draw.line(screen, GREEN, [0, 100], [100, 100], 5)
    # screen.blit(bg, [0, 0])
    # screen.blit(jet, [x, y])
    # ### End drawing zone
    # # update display
    # pygame.display.flip()

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
