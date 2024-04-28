import math
from enum import Enum
import os

class GameState(Enum):
    MAIN_MENU = 1
    GAMEPLAY = 2
    PAUSED = 3

# file paths
GAME_DIRECTORY = os.getcwd()
ASSETS_DIRECTORY = os.path.join(GAME_DIRECTORY, "assets")
TEXTURES_DIRECTORY = os.path.join(ASSETS_DIRECTORY, "textures")

# database names
TEST_REALM = "testrealm"

# game settings
RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60

PLAYER_POS = 1.5, 5 # mini_map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 50

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2