import pygame

class Shape():
    def __init__(self, surface, pos, w, h, color="cyan"):
        self.surface = surface
        self.pos = pos
        self.color = color 
        self.rect = pygame.Rect(self.pos.x, self.pos.y, w, h)
    def render(self): pass

class Rectangle(Shape):
    def render(self):
        return pygame.draw.rect(self.surface, self.color, self.rect)