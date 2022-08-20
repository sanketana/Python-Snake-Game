import sys
 
import pygame
from pygame.locals import *
from snake import Snake
from food import Food
 
pygame.init()
 
fps = 15
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

olive = Snake()
snack = Food()
 
# Game loop.
while True:
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN:
        if event.key == K_RIGHT:
            olive.direction = 'R'
        if event.key == K_LEFT:
            olive.direction = 'L'
        if event.key == K_UP:
            olive.direction = 'U'
        if event.key == K_DOWN:
            olive.direction = 'D'
  
  # Update.
  olive.move()
  if olive.munched(snack):
    print('Yummy')
    olive.grow = True
    snack.teleport()
    print(olive.grow)
  
  # Draw.
  olive.draw(screen)
  snack.draw(screen)
  
  pygame.display.flip()
  fpsClock.tick(fps)