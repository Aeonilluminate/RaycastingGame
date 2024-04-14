import pygame as pg
from settings import *

class Main_Menu:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.font = pg.font.Font(None, 40)  # Use Pygame's default font
        self.options = ["New Game", "Load Game", "Achievements", "Quit Game"]
        self.current_option = 0

    def draw(self):
        self.screen.fill('black')  # Clear the screen or set a background
        for i, option in enumerate(self.options):
            if i == self.current_option:
                label = self.font.render(option, True, (255, 0, 0))  # Highlighted in red
            else:
                label = self.font.render(option, True, (255, 255, 255))  # Others in white
            position = label.get_rect(center=(RES[0] / 2, 150 + i * 50))
            self.screen.blit(label, position)

    def handle_input(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.current_option = (self.current_option - 1) % len(self.options)
                elif event.key == pg.K_DOWN:
                    self.current_option = (self.current_option + 1) % len(self.options)
                elif event.key == pg.K_RETURN:
                    self.select_option()

    def select_option(self):
        if self.current_option == 0:  # New Game
            self.game.map.load_map("D:\\Dev\\PyCharm\\RaycastingGame\\assets\\maps\\level1.json")
            self.game.object_renderer.update()
            self.game.raycasting.textures = self.game.object_renderer.wall_textures
            self.game.game_state = GameState.GAMEPLAY
        elif self.current_option == 1:  # Load Game
            pass  # Implement loading functionality
        elif self.current_option == 2:  # Achievements
            pass  # Implement achievements display
        elif self.current_option == 3:  # Quit Game
            pg.quit()
            exit()

    def update(self, events):
        self.handle_input(events)

class Pause_Menu:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.font = pg.font.Font(None, 40)  # Use Pygame's default font
        self.options = ["Resume", "Save Game", "Achievements", "Quit Game"]
        self.current_option = 0

    def draw(self):
        self.screen.fill('black')  # Clear the screen or set a background
        for i, option in enumerate(self.options):
            if i == self.current_option:
                label = self.font.render(option, True, (255, 0, 0))  # Highlighted in red
            else:
                label = self.font.render(option, True, (255, 255, 255))  # Others in white
            position = label.get_rect(center=(RES[0] / 2, 150 + i * 50))
            self.screen.blit(label, position)


    def handle_input(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p: # Unpause condition
                    self.game.game_state = GameState.GAMEPLAY
                if event.key == pg.K_UP:
                    self.current_option = (self.current_option - 1) % len(self.options)
                elif event.key == pg.K_DOWN:
                    self.current_option = (self.current_option + 1) % len(self.options)
                elif event.key == pg.K_RETURN:
                    self.select_option()

    def select_option(self):
        if self.current_option == 0:  # Resume Game
            self.game.game_state = GameState.GAMEPLAY
        elif self.current_option == 1:  # Save Game
            pass  # Implement loading functionality
        elif self.current_option == 2:  # Achievements
            pass  # Implement achievements display
        elif self.current_option == 3:  # Quit Game
            pg.quit()
            exit()

    def update(self, events):
        self.handle_input(events)