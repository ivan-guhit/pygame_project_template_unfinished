import pygame

from pygame import Vector2



class Animation():
    def __init__(self, speed, pos, frame, size, spriteshet, frame_length, h=0):
        self.speed = speed
        self.pos = pos
        self.frame = frame
        self.tile_size = size
        self.frame_speed = speed
        self.frame_length = frame_length
        self.spriteshet = spriteshet
        self.h = h

    
    def play(self, surface):

        frame_loc = Vector2(int(self.frame), int(self.h)).elementwise() * self.tile_size
        frame_point = pygame.Rect(frame_loc.x, frame_loc.y, self.tile_size.x, self.tile_size.y)

        self.frame += self.frame_speed

        if self.frame >= self.frame_length:
            self.frame = 0

        surface.blit(self.spriteshet, self.pos, frame_point)




        