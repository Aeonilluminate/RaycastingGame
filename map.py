import pygame as pg
import json

class Map:
    def __init__(self, game, map_file):
        self.game = game
        self.map_data = self.load_map(map_file)
        self.world_map = {}
        self.get_map()

    def load_map(self, map_file):
        with open(map_file, 'r') as file:
            return json.load(file)

    def get_map(self):
        self.mini_map = self.map_data["map"]
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    # def get_textures(self):
        

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgrey', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]