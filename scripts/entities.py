import pygame

from pygame import Vector2

class PhysicsEntity():
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.e_type = e_type
        self.pos = pos
        self.size = size
 

        self.velocity = Vector2(0,0)
        self.crop_img = pygame.Rect(self.size.x, self.size.y, 32, 32)
        self.down = False
        self.jumped = False


    def rect(self):
        return pygame.Rect(int(self.pos.x), int(self.pos.y), int(self.size.x), 32)

    def update(self, tile, movement):

        frame_movementX = movement.x + self.velocity.x
        frame_movementY = movement.y + self.velocity.y

        self.my_rect = self.rect()

        self.pos.x += frame_movementX

        self.pos.y += frame_movementY

        

        
        
        #self.velocity.y = min(7, self.velocity.y + 0.2)

        if self.down == True or self.jumped == True:
            self.velocity.y = 0
    
    def render(self, surface):
        surface.blit(self.game.assets['player'], self.pos, self.crop_img)


