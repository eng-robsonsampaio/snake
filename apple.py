import pygame
import random
from pygame.locals import *

class Apple:

    def __init__(self, screen_size, size=(10, 10), color=(255, 0, 0)):
        
        self.scren_size = screen_size
        self.size = size
        self.position = (0, 0)
        self.surface = pygame.Surface(size)
        self.surface.fill(color)
    
    def set_random_position(self, screen_size):
        self.position = (random.randrange(0, screen_size-10, 10), random.randrange(0, screen_size-10, 10))
    
    