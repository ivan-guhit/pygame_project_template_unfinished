import pygame

from pygame import Vector2

class TileMap():
    def __init__(self, game, tile_size):
        self.list_of_pos = {}
        self.tile_size = tile_size
        self.game = game

        for i in range(10):
            self.list_of_pos[f'pos_{i}'] = Vector2(0+i,4)
            
    def render(self, surface):
        
        frame = 0
        for position in self.list_of_pos.values():

            sprite_loc = position.elementwise() * self.tile_size
            texture_frame = Vector2(frame,0).elementwise() * self.tile_size
            texture_rect = pygame.Rect(int(texture_frame.x), int(texture_frame.y), int(self.tile_size.x), int(self.tile_size.y))
            surface.blit(self.game.assets['ground'], sprite_loc, texture_rect)

            frame += 1
            
            


    
    
        
        

            


        



