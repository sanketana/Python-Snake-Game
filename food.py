import pygame
import random

class Food:
    color = (255, 0, 0)
    grid_x = 25
    grid_y = 16   


    def __init__(self, gridsize):
        self.size = gridsize
        self.size = gridsize
        self.x, self.y = self.grid_x * gridsize, self.grid_y * gridsize        
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)         

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)    
        pygame.draw.rect(screen, self.color, self.rect)    

    def teleport(self):
        self.x = self.size * random.randint(0, 40)
        self.y = self.size * random.randint(0, 30)   
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size) 