import pygame as pg
from settings import *

class Menu:
    def __init__(self, game, options):
        self.game = game
        self.screen = game.screen
        self.font = pg.font.Font(None, 40)  # Use Pygame's default font
        self.options = options
        self.current_option = 0

    def draw(self):
        self.screen.fill('black')  # Clear the screen or set a background
        for i, option in enumerate(self.options):
            color = (255, 0, 0) if i == self.current_option else (255, 255, 255)
            label = self.font.render(option, True, color)
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
        raise NotImplementedError("This method should be overridden by subclasses")

    def update(self, events):
        self.handle_input(events)

class Main_Menu(Menu):
    def __init__(self, game):
        super().__init__(game, ["New Game", "Load Game", "Achievements", "Quit Game"])

    def select_option(self):
        # Implement the specific actions for Main Menu
        options = {
            0: self.start_new_game,
            1: self.load_game,
            2: self.show_achievements,
            3: self.quit_game
        }
        options[self.current_option]()

    def start_new_game(self):
        self.game.map.load_map(os.path.join(ASSETS_DIRECTORY, "level_data", "Test.json"))
        self.game.object_renderer.update()
        self.game.raycasting.textures = self.game.object_renderer.wall_textures
        self.game.game_state = GameState.GAMEPLAY
        pass

    def load_game(self):
        # Implement load game functionality
        pass

    def show_achievements(self):
        # Implement achievements display
        pass

    def quit_game(self):
        pg.quit()
        exit()

class Pause_Menu(Menu):
    def __init__(self, game):
        super().__init__(game, ["Resume", "Save Game", "Achievements", "Quit Game"])

    def select_option(self):
        # Implement the specific actions for Pause Menu
        options = {
            0: self.resume_game,
            1: self.save_game,
            2: self.show_achievements,
            3: self.quit_game
        }
        options[self.current_option]()

    def resume_game(self):
        self.game.game_state = GameState.GAMEPLAY

    def save_game(self):
        # Implement save game functionality
        pass

    def show_achievements(self):
        # Same as in Main Menu, could further reduce redundancy
        pass

    def quit_game(self):
        pg.quit()
        exit()

    def update(self, events):
        self.handle_input(events)