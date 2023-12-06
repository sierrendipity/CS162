import pygame
import random
from settings import*
from spritesheet import Spritesheet

class Block(pygame.sprite.Sprite, Spritesheet):
    """3 different rocks that are selected at random"""

    def __init__(self, game, x, y):
        """initializes block attributes"""
        
        pygame.sprite.Sprite.__init__(self)
        Spritesheet.__init__(self, 'images/terrain.png')

        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        block_1 = [960, 448]
        block_2 = [992, 609]
        block_3 = [930, 448]
        block_list = [block_1, block_2, block_3]
        block = random.choice(block_list)

        self.image = self.get_sprite(block[0], block[1], self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Tree(pygame.sprite.Sprite):
    """3 different props/trees that are selected at random"""

    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.trees
        pygame.sprite.Sprite. __init__(self,self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        tree_1 = [136, 66]
        tree_2 = [84, 0]
        tree_3 = [120, 0]
        tree_list = [tree_1, tree_2, tree_3]
        tree = random.choice(tree_list)

        self.image = self.game.props_spritesheet.get_sprite(tree[0], tree[1], self.width, self. height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y 
     
class Ground(pygame.sprite.Sprite):
    """3 different ground squares that are selected at random"""

    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite. __init__(self,self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        block_1 = [0, 352]
        block_2 = [32, 352]
        block_3 = [64, 352]
        block_4 = [96, 352]
        block_list = [block_1, block_2, block_3, block_4]
        block = random.choice(block_list)

        self.image = self.game.terrain_spritesheet.get_sprite(block[0], block[1], self.width, self. height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y 