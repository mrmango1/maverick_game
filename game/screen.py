import pygame
from pygame import display
from game.settings import Settings
from game.game_menu import GameMenu


class Screen:
    MENU = 0
    GAME = 1

    def __init__(self) -> None:
        pygame.init()
        self.screen = 0
        self.settings = Settings()
        # Set the game image background
        self.game_screen = display.set_mode((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        # Initialize Settings Class
        self.menu = GameMenu(self.game_screen)
        # Initialize the loop variable
        self.run = True
        # Initialize the clock of the game (fps handler)
        self.clock = pygame.time.Clock()
        # Set the title game
        pygame.display.set_caption(self.settings.gameCaption)

    def run_game(self) -> None:
        self.menu.run_menu()
