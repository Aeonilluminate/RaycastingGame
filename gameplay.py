import pygame as pg
from settings import *

class Playing:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
    


    def update(self, keys):
        self.game.player.update(keys)
        self.game.raycasting.update()