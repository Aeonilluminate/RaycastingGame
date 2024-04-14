import pygame as pg
import json

class Map:
    def __init__(self, game):
        self.game = game
        self.map_data = None
        self.texture_data = None
        self.world_map = {}

    def load_map(self, map_file):
        with open(map_file, 'r') as file:
            self.map_data = json.load(file)
        
        self.asset_path = self.map_data["metadata"]["asset_path"]

        self.mini_map = self.map_data["map"]
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
        
        self.texture_data = {int(key):self.asset_path + "\\textures\\" + value 
                             for (key,value) in self.map_data["legend"].items()}
        print(f'Texture Data: {self.texture_data}') 

    def get_texture_data(self):
        return self.texture_data

    # def get_textures(self):
        
    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgrey', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]