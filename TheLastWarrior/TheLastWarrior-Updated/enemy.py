from spritesheet import Spritesheet
import pygame
from settings import *
import math
import random

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