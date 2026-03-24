import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

from pygame import Vector2
from scripts.entities import PhysicsEntity
from scripts.tilemap import TileMap
from scripts.utils import load_image, load_images


class Game():
    def __init__(self):
        pygame.init()

        self.cell_size = Vector2(64, 64)
        self.tile_size = Vector2(32, 32)
        self.tile_layout = Vector2(8,5).elementwise() * self.tile_size
        self.window_size = Vector2(16, 10).elementwise() * self.cell_size
        self.window = pygame.display.set_mode((int(self.window_size.x), int(self.window_size.y)))
        self.surface = pygame.Surface((int(self.tile_layout.x),int(self.tile_layout.y)))
        
        pygame.display.set_caption('Pygame Project')

        self.gameloop = True
        self.clock = pygame.time.Clock()
        self.p_size = Vector2(32, 32)

        self.assets = {
            'player' : load_image('player/sample.png'),
            'ground' : load_images('world/sample.png')
        }

        self.player_pos = Vector2(5,5)
        self.tile = TileMap(self, self.tile_size)
        self.player = PhysicsEntity(self, 'player', self.player_pos, self.p_size, self.tile)
        self.velocity = Vector2(0,0)

        

    def input_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameloop = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameloop = False
                    break
                if event.key == pygame.K_d:
                    self.velocity.x = 1
                if event.key == pygame.K_a:
                    self.velocity.x = -1
                if event.key == pygame.K_s:
                    self.velocity.y = 0
                if event.key == pygame.K_w:
                    self.velocity.y = 0
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.velocity.x = 0
                if event.key == pygame.K_a:
                    self.velocity.x = 0
                if event.key == pygame.K_s:
                    self.velocity.y = 0
                if event.key == pygame.K_w:
                    self.velocity.y = 0

        #print(self.velocity)

    def update(self):
        self.player.update(self.velocity)

    def render(self):
        self.surface.fill((0, 189, 0))
    
        
        self.player.render(self.surface)
        
        self.tile.render(self.surface)

        self.window.blit(pygame.transform.scale(self.surface, self.window.get_size()), (0,0))
        pygame.display.update()

    def run(self):
        while self.gameloop:
            self.input_handle()
            self.update()
            self.render()
            self.clock.tick(60)


game = Game()

game.run()

quit()