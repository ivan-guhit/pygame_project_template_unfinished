import pygame

from pygame import Vector2

LOCLOC = 'data/images/'

def load_image(path):
    img = pygame.image.load(LOCLOC + path)
    return img

def load_images(path):
    img = pygame.image.load(LOCLOC + path)
    return img
    
