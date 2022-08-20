import pygame
import random

class Food:
    size = 15
    color = (255, 0, 0)
    x = random.randint(15, 640-15)
    y = random.randint(15, 480-15)   
    rect = pygame.Rect(x, y, size, size) 

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)    

    def teleport(self):
        self.x = random.randint(15, 640-15)
        self.y = random.randint(15, 480-15)   
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size) 