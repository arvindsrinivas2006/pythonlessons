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
import utility

if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

MAX_SHOTS = 2  # most player bullets onscreen
ALIEN_ODDS = 22  # chances a new alien appears
BOMB_ODDS = 60  # chances a new bomb will drop
ALIEN_RELOAD = 12  # frames between new aliens
SCRRENRECT = Rect(0, 0, 1024, 768)
SCORE = 0

main_directory = os.path.split(os.path.abspath(__file__))[0]
def main(winstyle=o):
    if pygame.get_sdl_version()[0] == 2:
        pygame.mixer.pre_init(44100, 32, 2, 1024)
        
    pygame.init()

    if pygame.mixer and not pygame.mixer.get_init():
        print('Warning, no sound')
        pygame.mixer = None

    fullscreen = False
    winstyle = 0
    bestdepth = pygame.display.mode_ok
    (SCRRENRECT.size, winstyle, 32)

    screen = pygame.display.set_mode
    (SCRRENRECT.size, winstyle, bestdepth)
    player_image = utility.load_image('player1.gif')

    Player.images = [player_image, pygame.transform.flip
    (player_image, 1, 0)]
    explosion_image = utility.load_image('explosion1.gif')

    Explosion.images = [explosion_image,
    pygame.transform.flip
    (explosion_image, 1, 1)]
    Alien.images = utility.load_images(
        'alien1.gif',  'alien2.gif',  'alien3.gif')

    Bomb.images = [utility.load_image('bomb.gif')]
    Shot.images = [utility.load_image('shot.gif')]

    icon = pygame.transform.scale(Alien.images[0], (32, 32))

    pygame.display.set_icon(icon)

    pygame.display.set_caption("Arvind\'s Aliens Game")

    pygame.mouse.set_visible(0)

    background_image_tile = utility.load_image("background.gif")

    background = pygame.Surface(SCRRENRECT.size)

    for x_position in range(0, SCRRENRECT.width, background_image_tile.get_width()):
        background.blit(background_image_tile, (x_position, 0))
    
    screen.blit(background, (0,0))

    pygame.display.flip()

    boom_sound = utility.load_sound("boom.wav")
    shoot_sound = utility.load_sound("car_door.wav")

    if pygame.mixer:
        music = os.path.join(main_directory, "data", "house_lo.wav")

        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)
    
    aliens = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    bombs = pygame.sprite.Group()

    all_rects = pygame.sprite.RenderUpdates() 
    last_alien = pygame.sprite.GroupSingle()

    Player.containers = all
    Alien.containers = aliens, all, last_alien
    Shot.containers = shots, all
    Bomb.containers = bombs, all
    Explosion.containers = all
    Score.containers = all
    PlayerLives.containers = all

    alien_reload = ALIEN_RELOAD
    kills = 0
    clock = pygame.time.Clock()

    global SCORE

    player = Player(SCRRENRECT)

    Alien(SCRRENRECT)

    if pygame.font:
        all.add(Score())
        all.add(PlayerLives())
        


        
        

