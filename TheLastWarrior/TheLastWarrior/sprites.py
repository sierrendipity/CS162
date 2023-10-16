"""
File: Week 2
Author: Sierra Brightly
Student ID: X00465282
Date:October 7, 2023

Description:
Welcome to The Last Warrior! 
This is a mini RPG. In this game, you can choose between four characters. 
Once you've made your choice it's your job to kill all the enemies with the three 
lives you are given. 

This file is for all of the sprites in the game, inclduing the player, 
enemy, trees and, ground. 

"""

import pygame
from config import *
import math
import random

class Spritesheet:
    """general spritesheet class"""

    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width,height])
        # blit copies content of on surface to another
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite

class Player(pygame.sprite.Sprite):
    """ Player class paramters: pygame.sprite.Sprite"""

    def __init__(self, game, x, y):
        """initializes the playerparamters: self, game, x, y """

        # reset enemy count every time player is reinitialized
        # global ENEMY_COUNT
        # ENEMY_COUNT = 10
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

            # pygame.time.wait(100)

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

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        """Initializing enemy """

        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = random.choice(['down', 'up', 'left', 'right'])
        self.animation_loop = 0
        self.max_travel = random.randint(7, 30)

        self.image = self.game.enemy_spritesheet.get_sprite(0, 0, self.width, self.height)
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        # New attributes for seeking behavior
        self.follow_speed = .25  # Adjust the follow speed as needed
        self.max_speed = 1  # Maximum speed to avoid sudden stops
        self.max_force = 0.1  # Maximum steering force
        self.follow_range = 1  # Adjust this range as needed

    def update(self):
            
        self.move()
        self.animate()
        self.seek_player()
        
    # def movement_predetermined(self):
    #     """Predetermined movement for enemy"""

    #     if self.facing == 'down':
    #         self.y_change -= ENEMY_SPEED
    #         self.animation_loop += 1
    #         if self.animation_loop >= self.max_travel:
    #             self.facing = 'up'

    #     if self.facing == 'up':
    #         self.y_change += ENEMY_SPEED
    #         self.animation_loop += 1
    #         if self.animation_loop >= self.max_travel:
    #             self.facing = 'down'

    #     if self.facing == 'left':
    #         self.x_change -= ENEMY_SPEED
    #         self.animation_loop += 1
    #         if self.animation_loop >= self.max_travel:
    #             self.facing = 'right'

    #     if self.facing == 'right':
    #         self.x_change += ENEMY_SPEED
    #         self.animation_loop += 1
    #         if self.animation_loop >= self.max_travel:
    #             self.facing = 'left'

    def seek_player(self):
        player = self.game.player
        dx = player.rect.x - self.rect.x
        dy = player.rect.y - self.rect.y
        dist = math.sqrt(dx ** 2 + dy ** 2)

        if dist > 0:
            # Normalize the direction vector
            dx /= dist
            dy /= dist

            # Calculate the desired velocity towards the player
            desired_velocity_x = dx * self.max_speed
            desired_velocity_y = dy * self.max_speed

            # Calculate the steering force required to reach the desired velocity
            steering_x = desired_velocity_x - self.x_change
            steering_y = desired_velocity_y - self.y_change

            # Limit the steering force to the maximum force
            steering_mag = math.sqrt(steering_x ** 2 + steering_y ** 2)
            if steering_mag > self.max_force:
                scale = self.max_force / steering_mag
                steering_x *= scale
                steering_y *= scale

            # Apply the steering force
            self.x_change += steering_x
            self.y_change += steering_y

    def move(self):
        # Update the position based on the adjusted velocity
        self.rect.x += self.x_change
        self.rect.y += self.y_change

    def animate(self):
        """Animation for enemy movement"""

        animations = {
            'up': [self.game.enemy_spritesheet.get_sprite(x, 96, self.width, self.height) for x in range(0, 96, 32)],
            'down': [self.game.enemy_spritesheet.get_sprite(x, 0, self.width, self.height) for x in range(0, 96, 32)],
            'left': [self.game.enemy_spritesheet.get_sprite(x, 32, self.width, self.height) for x in range(0, 96, 32)],
            'right': [self.game.enemy_spritesheet.get_sprite(x, 64, self.width, self.height) for x in range(0, 96, 32)]
        }

        if self.facing in animations:
            if self.x_change != 0 or self.y_change != 0:
                # Update animation frame
                self.animation_loop = (self.animation_loop + 1) % len(animations[self.facing])
                self.image = animations[self.facing][self.animation_loop]
            else:
                # Set the default image when not moving
                self.image = animations[self.facing][0]

class Block(pygame.sprite.Sprite):
    """3 different rocks that are selected at random"""

    def __init__(self, game, x, y):
        """initializes block attributes"""
        
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite. __init__(self,self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        block_1 = [960, 448]
        block_2 = [992, 609]
        block_3 = [930, 448]
        block_list = [block_1, block_2, block_3]
        block = random.choice(block_list)

        self.image = self.game.terrain_spritesheet.get_sprite(block[0], block[1], self.width, self. height)
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

class Attack(pygame.sprite.Sprite):
    """Class for attacking an enemy"""

    def __init__(self, game, x, y):
        """initializes arributes needed for attack"""

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0 
        self.y_change = 0

        self.animation_loop = 0
        if self.animation_loop == 0:
            self.collidable = True

        self.image = self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height) 
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        # initializes player score (enemies killed) 
        self.score = 0

    def update(self):
        """update function"""
        self.animate()
        self.collide()

    def collide(self):
        """if attack collides with an enemy, enemy count -1 and update player's score"""

        if self.collidable:
            hits = pygame.sprite.spritecollide(self, self.game.enemies, True)
            if hits:
                self.game.player.score += 1  # Increase player's score
                print(f"Player Score: {self.game.player.score}")  # Print the updated score

        pygame.display.update()


    def animate(self):
        """anmiamtion for attack motion"""
        direction = self.game.player.facing

        right_animations = [self.game.attack_spritesheet.get_sprite(0, 64, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(32, 64, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(64, 64, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(96, 64, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(128, 64, self.width, self.height)]

        down_animations = [self.game.attack_spritesheet.get_sprite(0, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(32, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(64, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(96, 32, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(128, 32, self.width, self.height)]

        left_animations = [self.game.attack_spritesheet.get_sprite(0, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(32, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(64, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(96, 96, self.width, self.height),
                           self.game.attack_spritesheet.get_sprite(128, 96, self.width, self.height)]

        up_animations = [self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(32, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(64, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(96, 0, self.width, self.height),
                         self.game.attack_spritesheet.get_sprite(128, 0, self.width, self.height)]

        if direction == 'up':
            self.image = up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
        if direction == 'down':
            self.image = down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
        if direction == 'left':
            self.image = left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
        if direction == 'right':
            self.image = right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
