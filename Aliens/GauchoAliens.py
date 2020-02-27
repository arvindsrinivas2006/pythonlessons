import random
import os.path

import pygame
from pygame.locals import *

from Alien import Alien
from SpongeAlien import SpongeAlien
from bomb import Bomb
from BubbleShield import BubbleShield
from BubbleShieldBox import BubbleShieldBox
from Explosion import Explosion
from GameLevel import GameLevel
from Player import Player
from PlayerLives import PlayerLives
from SpaceMonster import SpaceMonster
from Score import Score
from Shot import Shot
import utility
from GreenAlien import GreenAlien

if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

DISPLAY_WIDTH = 1024
DISPLAY_HEIGHT= 768
MAX_SHOTS = 2  # most player bullets onscreen
ALIEN_ODDS = 22  # chances a new alien appears
BLACK = (0, 0, 0)  # Red, Green, Blue, absence of color!
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
    sponge_aliens = pygame.sprite.Group()
    green_aliens = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    bombs = pygame.sprite.Group()


    all_game_rects = pygame.sprite.RenderUpdates() 
    last_alien = pygame.sprite.GroupSingle()

    BubbleShield.containers = all_game_rects
    BubbleShieldBox.containers = all_game_rects
    Player.containers = all_game_rects
    Alien.containers = aliens, all_game_rects, last_alien
    GreenAlien.containers = green_aliens, all_game_rects
    Shot.containers = shots, all_game_rects
    Bomb.containers = bombs, all_game_rects
    Explosion.containers = all_game_rects
    Score.containers = all_game_rects
    Score.score_points = 0
    GameLevel.containers = all_game_rects
    GameLevel.level = 1
    PlayerLives.containers = all_game_rects
    PlayerLives.lives = 3

    SpongeAlien.containers = aliens, all_game_rects, last_alien


    Alien(SCREENRECT)

    if pygame.font is not None:
        all_game_rects.add(Score())
        all_game_rects.add(GameLevel())
        all_game_rects.add(PlayerLives())

    clock = game_loop(all_game_rects, screen, background, shots, last_alien, aliens, green_aliens, bombs, winstyle, bestdepth, FULLSCREEN)

    game_over(screen, clock)

    quit_game()
    
def quit_game():
    # if pygame sound is running
    if (pygame.mixer is not None):
        pygame.mixer.music.fadeout(1000)

    pygame.time.wait(1000)

    pygame.quit()

    # quit pyton
    quit()

def button(screen, msg, x, y, width, height, ic, ac, action=None):
    mouse_position = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    # print(mouse_click)

    if (x + width > mouse_position[0] > x) and \
            (y+height > mouse_position[1] > y):

        pygame.draw.rect(screen, ac, (x, y, width, height))
        
        # is there a mouse click over the button
        if mouse_click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, width, height))

    # create button
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(width/2)), (y+(height/2)))

    screen.blit(textSurf, textRect)
    

def check_game_level(score):
    if(GameLevel.level == 1 and score > 10):
        GameLevel.level = 2
    elif(GameLevel.level == 2 and score > 20):
        GameLevel.level = 3
    elif(GameLevel.level == 3 and score > 30):
        GameLevel.level = 4
    
        
def game_loop(all_game_rects, screen, background, shots, last_alien, aliens, green_aliens, bombs, winstyle, bestdepth, FULLSCREEN):
    print("In GauchoAliens - game_loop()")

    clock = pygame.time.Clock()

    player = Player(SCREENRECT)
    
    alien_reload = ALIEN_RELOAD
    
    boom_sound = utility.load_sound("boom.wav")
    shoot_sound = utility.load_sound("car_door.wav")
    bubble_shield = BubbleShield(player)
    bubble_shield_box = BubbleShieldBox(SCREENRECT)
    shield_spawned = False
    shield_box_spawned = False
    
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
        handle_player_input(player, shots, bubble_shield, shoot_sound)

        if alien_reload:
            alien_reload = alien_reload - 1
        elif not int(random.random() * ALIEN_ODDS):
            alien_reload = ALIEN_RELOAD

            if(GameLevel.level == 3):
                SpongeAlien(SCREENRECT)
            if GameLevel.level == 4:
                GreenAlien(SCREENRECT)
            else:
                Alien(SCREENRECT)
            
        if last_alien and not int(random.random() * BOMB_ODDS):
            Bomb(last_alien.sprite)

        if(GameLevel.level == 1):
            if(shield_box_spawned is False):
                bubble_shield_box.is_active = True

                shield_box_spawned = True
        detect_collisions(player, aliens, shots, bombs, boom_sound, green_aliens)

        # draw the scene
        is_dirty = all_game_rects.draw(screen)
        pygame.display.update(is_dirty)
        clock.tick(40)
    
    return clock

def check_player_life(player):
    if (PlayerLives.lives < 1):
        # player is dead
        player.kill()

def detect_collisions(player, aliens, shots, bombs, boom_sound, green_aliens):
    for alien in pygame.sprite.spritecollide(player, aliens, 1):
        boom_sound.play()
        Explosion(alien)
        Explosion(player)
        Score.score_points = Score.score_points + 1
        check_game_level(Score.score_points)
        
        PlayerLives.lives = PlayerLives.lives - 1
     
        check_player_life(player)
         
    # alien vs tank shot
    for alien in pygame.sprite.groupcollide(shots,  aliens, 1, 1).keys():

        boom_sound.play()
        Explosion(alien)

        Score.score_points = Score.score_points + 1
        check_game_level(Score.score_points)
    # player vs alien bomb
    for bomb in pygame.sprite.spritecollide(player, bombs, 1):
        boom_sound.play()

        Explosion(player)
        Explosion(bomb)

        PlayerLives.lives = PlayerLives.lives - 1

        check_player_life(player)

    for bomb in pygame.sprite.groupcollide(shots, bombs, 1, 1).keys():
        boom_sound.play()
        Explosion(bomb)
        bomb.kill()

    for green_alien in pygame.sprite.groupcollide(shots, green_aliens, 1, 1).keys():
        boom_sound.play()
        Explosion(green_alien)
        Score.score_points = Score.score_points + 1
        check_game_level(Score.score_points)
        

   # player vs GreenAlien
    for green_alien in pygame.sprite.spritecollide(player, green_aliens, 1):
       Explosion(green_alien)
       boom_sound.play()

       Score.score_points = Score.score_points + 2

       check_game_level(Score.score_points)

       PlayerLives.lives = PlayerLives.lives - 1

       check_player_life(player)

        

        

def handle_player_input(player, shots, bubble_shield, shoot_sound):
    # print("In GauchoAliens - handle_player_input()")
    global MAX_SHOTS

    keystate = pygame.key.get_pressed() 
    
    direction = keystate[K_RIGHT] - keystate[K_LEFT]

    player.move(direction)

    if(bubble_shield.is_active is True):
        bubble_shield.move(player)
        
    firing = keystate[K_SPACE]

    if not player.reloading and firing and len(shots) < MAX_SHOTS:
        Shot(player.gunpos())
        shoot_sound.play()

    player.reloading = firing

def set_game_obj_images():
    player_image = utility.load_image('player1.gif')

    Player.images = [player_image, pygame.transform.flip(player_image, 1, 0)]
    
    bubble_shield_blank_box = utility.load_image_transparent_background("bubble shield blank box.png")
    bubble_shield_box = utility.load_image("bubble shield box.png")

    BubbleShieldBox.images = [
        bubble_shield_blank_box,
        bubble_shield_box
    ]
    explosion_image = utility.load_image('explosion1.gif')

    Explosion.images = [explosion_image,
    pygame.transform.flip
    (explosion_image, 1, 1)]
    Alien.images = utility.load_images(
        'alien1.gif',  'alien2.gif',  'alien3.gif')
    # level 3 Aliens
    SpongeAlien.images = utility.load_images(
        "sponge_alien1.png",
        "sponge_alien2.png",
        "sponge_alien3.png"
    )
    #  level 4 GreenAlien
    green_alien_image = utility.load_image("GreenAlien.png")

    GreenAlien.images = [
                            green_alien_image,
                            pygame.transform.flip(green_alien_image,
                            1, 0),
                            green_alien_image
    ]

    # level 5 space monster
    space_monster_image = utility.load_image_transparent_background(
        "spacemonster.png")
    agro_monster_image = utility.load_image_transparent_background(
        "spacemonster - agro.png")
        
    bubble_shield_blank = utility.load_image_transparent_background(
        "bubble shield blank.png")

    bubble_shield = utility.load_image_transparent_background(
        "bubble shield.png")

    BubbleShield.images = [bubble_shield_blank, bubble_shield]
    
                                        
    

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

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)

    return textSurface, textSurface.get_rect()





def game_over(screen, clock):
    bright_red = (255, 0, 0)
    bright_green = (0, 255, 0)
    green = (77, 206, 30)
    white = (84, 121, 130)
    red = (255, 0, 0)
    is_game_over = True

    # show the mouse cursor
    pygame.mouse.set_visible(1)

    while is_game_over is True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                quit_game()

        # set the background color for gameover screen
        screen.fill(white)

        largeText = pygame.font.Font('freesansbold.ttf', 115)
        medium_text = pygame.font.Font('freesansbold.ttf', 100)

        TextSurf, TextRect = text_objects("Game Over", largeText)
        TextRect.center = ((DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/2))
        screen.blit(TextSurf, TextRect)

        score_text = "Score: " + str(Score.score_points)

        scoreSurf, scoreRect = text_objects(score_text, medium_text)

        scoreRect.center = ((DISPLAY_WIDTH/4), (DISPLAY_HEIGHT/4))

        screen.blit(scoreSurf, scoreRect)

        level_text = "Level: " + str(GameLevel.level)

        levelSurf, levelRect = text_objects(level_text, medium_text)

        levelRect.center = ((DISPLAY_WIDTH * .75), (DISPLAY_HEIGHT/
        4))

        screen.blit(levelSurf, levelRect)

        # mouse = pygame.mouse.get_pos()

        # print(mouse)

        button(screen, "Play Again!", 150, 450, 100, 50,
               green, bright_green, main)
               
                
        button(screen, "Quit", 550, 450, 100, 50, red, bright_red,
        quit_game)

        pygame.display.update()
        clock.tick(15)

    # call the "main" function if running this script
if (__name__ == "__main__"):
    main()


