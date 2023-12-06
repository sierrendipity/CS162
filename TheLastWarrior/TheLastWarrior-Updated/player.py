from spritesheet import Spritesheet
import pygame
from settings import *
import math

class Player(pygame.sprite.Sprite):
    """ Player class paramters: pygame.sprite.Sprite"""

    def __init__(self, game, x, y):
        """initializes the playerparamters: self, game, x, y """

        self.game = game

        #player will be drawn above everything
        self._layer = PLAYER_LAYER

        #adding play to all_sprites group with game as an object
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        #position and direction
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0 
        self.y_change = 0

        self.facing = 'down'
        self.animation_loop = 1

        self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)

        #this is the "hitbox" location and is the same size of the image
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        # initializes player lives
        self.lives = 3

        self.score = 0


    def update(self):
        """update function for player"""

        self.movement()
        self.animate()
        self.collide_enemy()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.collide_trees('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.collide_trees('y')

        self.x_change = 0
        self.y_change = 0
       
    def movement(self):
        """movement of player function, this is with a 'camera' that will move with the player"""

        keys = pygame.key.get_pressed()

        # Create temporary variables for player's intended movement
        x_change_temp = 0
        y_change_temp = 0

        if keys[pygame.K_a]:
            x_change_temp -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_d]:
            x_change_temp += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_w]:
            y_change_temp -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_s]:
            y_change_temp += PLAYER_SPEED
            self.facing = 'down'

        # Check for collisions in the intended direction
        self.rect.x += x_change_temp
        self.rect.y += y_change_temp

        # Check for collisions with blocks and trees
        block_collisions_x = pygame.sprite.spritecollide(self, self.game.blocks, False)
        tree_collisions_x = pygame.sprite.spritecollide(self, self.game.trees, False)

        self.rect.x -= x_change_temp
        self.rect.y -= y_change_temp

        # If there are no collisions in the intended direction, update player's movement
        if not block_collisions_x and not tree_collisions_x:
            self.x_change = x_change_temp
            self.y_change = y_change_temp

        # Move the camera based on player's movement
        for sprite in self.game.all_sprites:
            sprite.rect.x -= self.x_change
            sprite.rect.y -= self.y_change

    def collide_enemy(self):
        """if player collides with enemy, player will be knocked back. 
        This is done by moving the rest of the sprites to make it look like that."""

        hits = pygame.sprite.spritecollide(self,self.game.enemies, False)
        if hits:
            if self.facing == 'right':
                for sprite in self.game.all_sprites:
                    sprite.rect.x += PLAYER_SPEED * KNOCK_DISTANCE
                self.x_change -= PLAYER_SPEED * KNOCK_DISTANCE
            elif self.facing == 'left':
                for sprite in self.game.all_sprites:
                    sprite.rect.x -= PLAYER_SPEED * KNOCK_DISTANCE
                self.x_change += PLAYER_SPEED * KNOCK_DISTANCE
            elif self.facing == 'down':
                for sprite in self.game.all_sprites:
                    sprite.rect.y += PLAYER_SPEED * KNOCK_DISTANCE
                self.y_change -= PLAYER_SPEED * KNOCK_DISTANCE
            elif self.facing == 'up':
                for sprite in self.game.all_sprites:
                    sprite.rect.y -= PLAYER_SPEED * KNOCK_DISTANCE
                self.y_change += PLAYER_SPEED * KNOCK_DISTANCE


            self.lives -= 1
            # print(self.lives)
            if self.lives <= 0:
                self.game.playing = False
                
        pygame.display.update()

    def collide_blocks(self,direction):
        """if you run into a block, stop moving in that direction"""

        if direction =='x':
            hits = pygame.sprite.spritecollide(self,self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right 
        if direction =='y':
            hits = pygame.sprite.spritecollide(self,self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    def collide_trees(self,direction):
        """if you run into a "tree", stop moving in that direction"""

        if direction =='x':
            hits = pygame.sprite.spritecollide(self,self.game.trees, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right 
        if direction =='y':
            hits = pygame.sprite.spritecollide(self,self.game.trees, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    def animate(self):
        """Animates the walking function of the character"""

        down_animations = [self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(32, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 0, self.width, self.height)]

        up_animations = [self.game.character_spritesheet.get_sprite(0, 96, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(32, 96, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(64, 96, self.width, self.height)]

        left_animations = [self.game.character_spritesheet.get_sprite(0, 32, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(32, 32, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(64, 32, self.width, self.height)]

        right_animations = [self.game.character_spritesheet.get_sprite(0, 64, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(32, 64, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(64, 64, self.width, self.height)]  

        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height) 
            else:
                #moves every 10 frames through the different movement images
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 96, self.width, self.height) 
            else:
                #moves every 10 frames through the different movement images
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 32, self.width, self.height) 
            else:
                #moves every 10 frames through the different movement images
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 64, self.width, self.height) 
            else:
                #moves every 10 frames through the different movement images
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1