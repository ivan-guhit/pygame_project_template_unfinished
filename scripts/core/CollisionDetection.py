import pygame

class CollisionDetection():
    def __init__(self, entity, shape):
        self.entity = entity
        self.shape = shape
    
    def check_collision(self):
        return self.shape.rect.colliderect(self.entity.rect)

        # if self.shape.rect.colliderect(self.entity.rect):
        #     print("im collisioning bruv")