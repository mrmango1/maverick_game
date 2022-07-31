import pygame
from pygame.sprite import Group, groupcollide
from pygame import display, image, transform
from model.player.jet import JetPlayer
from model.enemy.jet import JetEnemy
from game.settings import Settings


class Maverick:
    def __init__(self):
        pygame.init()
        # Initialize Settings Class
        self.settings = Settings()
        # Initialize the loop variable
        self.run = True
        # Initialize the clock of the game (fps handler)
        self.clock = pygame.time.Clock()
        # Set the game image background
        self.__set_background(self.settings.backgroundImage)
        # Set the title game
        pygame.display.set_caption(self.settings.gameCaption)
        # Initialize the scroll background variable handler
        self.scroll = 0

        # Instance models and create sprite groups
        self.player = Group()
        self.enemies = Group()
        self.all_sprites = Group()

        self.player_list = [self.player, self.all_sprites]
        self.enemy_list = [self.enemies, self.all_sprites]

        self.jetPlayer = JetPlayer(self.settings.get_jet("ecuador"), self.player_list)
        self.jetEnemy = JetEnemy(self.settings.get_aleatory_jet(), self.enemy_list)

        self.player.add(self.jetPlayer)
        self.enemies.add(self.jetEnemy)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.enemies)

    def run_game(self):
        while self.run:
            self.clock.tick(self.settings.FPS)
            self.__background_move()
            self.all_sprites.update()
            self.__check_collisions()
            self.all_sprites.draw(self.game_screen)
            self.__check_events()
        pygame.quit()

    def __check_events(self):
        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
        pygame.display.update()

    def __check_collisions(self):
        # Filter Collisions
        hits = groupcollide(self.player, self.enemies, True, True)
        for first, second in hits.items():
            if not isinstance(first, type(second[0])) and not isinstance(first, type(self.jetPlayer)):
                self.jetEnemy = JetEnemy(self.settings.get_aleatory_jet(), self.enemy_list)
                self.enemies.add(self.jetEnemy)
                self.all_sprites.add(self.jetEnemy)
            if isinstance(first, type(self.jetPlayer)):
                self.run = False

    def __set_background(self, image_background: str) -> None:
        self.game_screen = display.set_mode((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        self.game_screen.fill(self.settings.WHITE)
        self.background = image.load(image_background).convert()
        self.background = transform.scale(self.background, (self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        self.background_rect = self.background.get_rect()

    def __background_move(self) -> None:
        for i in range(2):
            self.game_screen.blit(self.background, (i * self.settings.SCREEN_WIDTH + self.scroll, 0))
            self.background_rect.x = i * self.settings.SCREEN_WIDTH + self.scroll
        self.scroll -= 2
        # reset scroll
        if abs(self.scroll) > self.settings.SCREEN_WIDTH:
            self.scroll = 0
