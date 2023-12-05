import pygame
from settings import*
from support import import_folder
from random import choice


class AnimationPlayer:
    def __init__(self):

        self.frames = {

            #magic
            'flame': import_folder('media/graphics/particles/flame/frames'),
            'aura': import_folder('media/graphics/particles/aura'),
            'heal': import_folder('media/graphics/particles/heal/frames'),

            #attacks
            'claw': import_folder('media/graphics/particles/claw'),
            'slash': import_folder('media/graphics/particles/slash'),
            'sparkle': import_folder('media/graphics/particles/sparkle'),
            'leaf_attack': import_folder('media/graphics/particles/leaf_attack'),
            'thunder': import_folder('media/graphics/particles/thunder'),

            #monster deaths
            'squid': import_folder('media/graphics/particles/smoke_orange'),
            'raccoon': import_folder('media/graphics/particles/raccoon'),
            'spirit': import_folder('media/graphics/particles/nova'),
            'bamboo': import_folder('media/graphics/particles/bamboo'),

            #leaves
            'leaf': (
                import_folder('media/graphics/particles/leaf1'),
                import_folder('media/graphics/particles/leaf2'),
                import_folder('media/graphics/particles/leaf3'),
                import_folder('media/graphics/particles/leaf4'),
                import_folder('media/graphics/particles/leaf5'),
                import_folder('media/graphics/particles/leaf6'),
                self.reflect_images(import_folder('media/graphics/particles/leaf1')),
                self.reflect_images(import_folder('media/graphics/particles/leaf2')),
                self.reflect_images(import_folder('media/graphics/particles/leaf3')),
                self.reflect_images(import_folder('media/graphics/particles/leaf4')),
                self.reflect_images(import_folder('media/graphics/particles/leaf5')),
                self.reflect_images(import_folder('media/graphics/particles/leaf6')),
                )
        }

    def reflect_images(self,frames):
        new_frames = []
        for frame in frames:
            flipped_frame = pygame.transform.flip(frame,True,False)
            new_frames.append(flipped_frame)
        return new_frames
    
    def create_grass_particles(self,pos,groups):
        animation_frames = choice(self.frames['leaf'])
        ParticleEffect(pos,animation_frames,groups)

    def create_particles(self,animation_type,pos,groups):
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos,animation_frames,groups)

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self,pos,animation_frames,groups):

        #general set up
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()