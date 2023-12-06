import pygame
from settings import*

class Spritesheet:
    """general spritesheet class"""

    def __init__(self, file):
        try:
            self.sheet = pygame.image.load(file).convert()
        except pygame.error as e:
            print(f"Error loading spritesheet: {e}")

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width,height])
        # blit copies content of on surface to another
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite