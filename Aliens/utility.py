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

        images.append(image)
        
    return images

def load_image_transparent_background(file_name):
    file_path_name = os.path.join(main_directory, "data", file_name)

    try:
        surface = pygame.image.load(file_path_name)
    except pygame.error:
        raise SystemExit('Could not load image: ' + file_path_name)

        # raise SystemExit('Could not load image "%s" %s' %
        #                   (file_path_name, pygame.get_error()))

    return surface.convert_alpha()





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

