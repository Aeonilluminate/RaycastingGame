import pygame as pg
import sys
from settings import *
from menus import *
from map import *
from player import *
from raycasting import *
from object_renderer import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
        self.game_state = GameState.MAIN_MENU

    def new_game(self):
        self.menu = Main_Menu(self)
        self.paused = Pause_Menu(self)
        self.map = Map(self, "D:\\Dev\\PyCharm\\RaycastingGame\\assets\\maps\\level1.json")
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)

    def update(self, state, events=None):
        match state:
            case GameState.MAIN_MENU:
                self.menu.update(events)
                pg.display.flip()
            case GameState.GAMEPLAY:
                self.player.update()
                self.raycasting.update()
                pg.display.flip()
                self.delta_time = self.clock.tick(FPS)
                pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
            case GameState.PAUSED:
                self.paused.update(events)
                pg.display.flip()

    def draw(self, state):
        match state:
            case GameState.MAIN_MENU:
                self.menu.draw()
            case GameState.GAMEPLAY:
                self.screen.fill('black')
                self.object_renderer.draw()
            case GameState.PAUSED:
                self.paused.draw()

            # self.map.draw()
            # self.player.draw()

    def check_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if self.game_state is not GameState.MAIN_MENU and event.type == pg.KEYDOWN and event.key == pg.K_p:
                pg.event.clear() # Clears event queue so as to prevent the game from immediately unpausing by processing another input of the key "p"
                events = pg.event.get()
                self.game_state = GameState.PAUSED
        # Pass the events to the current state for further processing
        return events

    def run(self):
        while True:
            events = self.check_events()
            self.update(self.game_state, events)
            self.draw(self.game_state) 
                    

    def toggle_pause(self):
        if self.game_state == GameState.GAMEPLAY:
            self.game_state = GameState.PAUSED
        elif self.game_state == GameState.PAUSED:
            self.game_state = GameState.GAMEPLAY


if __name__ == '__main__':
    game = Game()
    game.run()