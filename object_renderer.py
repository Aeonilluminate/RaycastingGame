import pygame as pg
from settings import *
from map import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

    def draw(self):
        self.render_game_objects()

    def render_game_objects(self):
        list_objects = self.game.raycasting.objects_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('assets/textures/plant_wall1.png'),
            2: self.get_texture('assets/textures/Rowan_Raya_Lucaria.png'),
            3: self.get_texture('assets/textures/Elias_Goldhorn.png'),
            4: self.get_texture('assets/textures/Victoria_Edwards.png'),
            5: self.get_texture('assets/textures/Neo.png')
        }