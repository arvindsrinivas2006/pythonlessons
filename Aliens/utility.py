import os.path
import pygame
from pygame.locals import *


main_directory = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    file = os.path.join(main_directory,  'data', file)

    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image')

    return surface.convert()

def load_images(*files):
    images = []

    for file in files:
        image = load_image(file)

    return images

class DummySound:
    def play(self):
        pass

def load_sound(file):
    if not pygame.mixer:
        return DummySound()
    
    file = os.path.join(main_directory, "data", file)

    try:
        sound = pygame.mixer.Sound(file)

        return sound
    except pygame.error:
        print('Could not load sound, %s' % file)

    return DummySound()

