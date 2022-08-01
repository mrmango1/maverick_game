import pygame
import sys
from pygame.sprite import Group, groupcollide
from pygame import display, image, transform
from model.player.jet import JetPlayer
from model.enemy.jet import JetEnemy
from game.settings import Settings
from game.button import Button


class Maverick:
    def __init__(self, game_screen: pygame.display) -> None:
        pygame.init()
        self.game_screen = game_screen
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

    def run_game(self) -> int:
        while self.run:
            self.__background_move()
            self.__menu_button()
            self.__check_collisions()
            backToMenu = self.__handle_events()
            if backToMenu is not None:
                return backToMenu
        pygame.quit()

    def __handle_events(self) -> int:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.buttonBack.checkForInput(self.mousePosition):
                    return 0
        pygame.display.update()

    def __check_collisions(self) -> None:
        """
        It checks if the player collides with an enemy, if it does, it checks if the enemy is a jet, if it is,
        it creates a new jet enemy and adds it to the enemies group
        """
        self.all_sprites.update()
        hits = groupcollide(self.player, self.enemies, True, True)
        for first, second in hits.items():
            if not isinstance(first, type(second[0])) and not isinstance(first, type(self.jetPlayer)):
                self.jetEnemy = JetEnemy(self.settings.get_aleatory_jet(), self.enemy_list)
                self.enemies.add(self.jetEnemy)
                self.all_sprites.add(self.jetEnemy)
            if isinstance(first, type(self.jetPlayer)):
                self.run = False
                sys.exit()
        self.all_sprites.draw(self.game_screen)

    def __set_background(self, image_background: str) -> None:
        """
        This function sets the background image for the game

        :param image_background: The path to the image you want to use as the background
        :type image_background: str
        """
        self.game_screen = display.set_mode((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        self.background = image.load(image_background).convert()
        self.background = transform.scale(self.background, (self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        self.background_rect = self.background.get_rect()

    def __background_move(self) -> None:
        """
        The function blits the background image to the screen twice, and then moves the background image to the left
        by 2 pixels
        """
        self.clock.tick(self.settings.FPS)
        for i in range(2):
            self.game_screen.blit(self.background, (i * self.settings.SCREEN_WIDTH + self.scroll, 0))
            self.background_rect.x = i * self.settings.SCREEN_WIDTH + self.scroll
        self.scroll -= 2
        # reset scroll
        if abs(self.scroll) > self.settings.SCREEN_WIDTH:
            self.scroll = 0

    def __menu_button(self) -> None:
        self.mousePosition = pygame.mouse.get_pos()

        self.buttonBack = Button(image=None, pos=(40, 20),
                                 text_input="BACK", font=self.settings.get_font(25), base_color="White",
                                 hovering_color="Green")

        self.buttonBack.changeColor(self.mousePosition)
        self.buttonBack.update(self.game_screen)
