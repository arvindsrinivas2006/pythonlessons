import random
import os.path

import pygame
from pygame.locals import *

from Alien import Alien
from bomb import Bomb
from Explosion import Explosion
from Player import Player
from PlayerLives import PlayerLives
from Score import Score
from Shot import shot
from utility import *

if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

MAX_SHOTS = 2  # most player bullets onscreen
ALIEN_ODDS = 22  # chances a new alien appears
BOMB_ODDS = 60  # chances a new bomb will drop
ALIEN_RELOAD = 12  # frames between new aliens
