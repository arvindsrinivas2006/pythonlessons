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
from Shot import Shot
import utility

if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

MAX_SHOTS = 2  # most player bullets onscreen
ALIEN_ODDS = 22  # chances a new alien appears
BOMB_ODDS = 60  # chances a new bomb will drop
ALIEN_RELOAD = 12  # frames between new aliens
SCREENRECT = Rect(0, 0, 1024, 768)

main_directory = os.path.split(os.path.abspath(__file__))[0]

def main(winstyle=0):
    if pygame.get_sdl_version()[0] == 2:
        pygame.mixer.pre_init(44100, 32, 2, 1024)
        
    pygame.init()

    fullscreen = False
    winstyle = 0
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)

    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    set_game_obj_images()

    pygame.mouse.set_visible(0)

    background_image_tile = utility.load_image("background.gif")

    background = pygame.Surface(SCREENRECT.size)

    for x_position in range(0, SCREENRECT.width, background_image_tile.get_width()):
        background.blit(background_image_tile, (x_position, 0))
    
    screen.blit(background, (0,0))

    pygame.display.flip()

    set_game_sound()
    
    aliens = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    bombs = pygame.sprite.Group()

    all_game_rects = pygame.sprite.RenderUpdates() 
    last_alien = pygame.sprite.GroupSingle()

    Player.containers = all_game_rects
    Alien.containers = aliens, all_game_rects, last_alien
    Shot.containers = shots, all_game_rects
    Bomb.containers = bombs, all_game_rects
    Explosion.containers = all_game_rects
    Score.containers = all_game_rects
    PlayerLives.containers = all_game_rects

    Alien(SCREENRECT)

    if pygame.font is not None:
        # all_game_rects.add(Score())
        all_game_rects.add(PlayerLives())

    game_loop(all_game_rects, screen, background, shots, last_alien, aliens, bombs, winstyle, bestdepth, FULLSCREEN)

    # quit game
    # if pygame sound is running
    if (pygame.mixer is not None):
        pygame.mixer.music.fadeout(1000)

    pygame.time.wait(1000)

    pygame.quit()

        
def game_loop(all_game_rects, screen, background, shots, last_alien, aliens, bombs, winstyle, bestdepth, FULLSCREEN):
    clock = pygame.time.Clock()

    player = Player(SCREENRECT)
    
    alien_reload = ALIEN_RELOAD
    
    boom_sound = utility.load_sound("boom.wav")
    shoot_sound = utility.load_sound("car_door.wav")

    # establish player has 3 lives
    while (player.alive() is True):
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
            elif event.type == KEYDOWN:
                if event.key == pygame.K_f:
                    if not FULLSCREEN:
                        print("changing to fullscreen")
                        screen_backup = screen.copy()

                        screen = pygame.display.set_mode(SCREENRECT.size, winstyle | FULLSCREEN, bestdepth)
                        screen.blit(screen_backup, (0,0))
                    else:
                        print("Changing to windowed mode")
                        screen_backup = screen.copy()
                        screen = pygame.display.set_mode(
                            SCREENRECT.size,
                            winstyle,
                            bestdepth
                        )
                        screen.blit(screen_backup, (0,0))
                    
                    # screen.fill((255, 0, 0))
                    pygame.display.flip()
                    FULLSCREEN = not FULLSCREEN
            
        all_game_rects.clear(screen, background)
        all_game_rects.update()
        handle_player_input(player, shots, shoot_sound)

                    

def set_game_obj_images():
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



def set_game_sound():
    if pygame.mixer and not pygame.mixer.get_init():
        print('Warning, no sound')
        pygame.mixer = None
    
    if pygame.mixer:
        music = os.path.join(main_directory, "data", "house_lo.wav")

        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)

    

    # call the "main" function if running this script
if (__name__ == "__main__"):
    main()


