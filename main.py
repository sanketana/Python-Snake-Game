import sys
 
import pygame
from pygame.locals import *
from snake import Snake
from food import Food
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()

score = 0
GRIDSIZE = 10
width, height = GRIDSIZE * 45, GRIDSIZE * 32
screen = pygame.display.set_mode((width, height))

TICK = pygame.USEREVENT
pygame.time.set_timer(TICK, 100)

olive = Snake(GRIDSIZE)
snack = Food(GRIDSIZE)

gameState = 'Play'
snakeMove = False

def displayScore():
    global score
    font = pygame.font.Font(None, 45)
    score_surface = font.render("Score: " + str(score), True, (0, 0, 255))
    screen.blit(score_surface, (20, 20))


def gameOn():
  global snakeMove
  global gameState
  global score

  # Game loop.
  print('Inside gameplay')
  while True:
    if gameState == 'Play':
      screen.fill((0, 0, 0))
      
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
            snakeMove = True
            if event.key == K_RIGHT:
                olive.direction = 'R'
            if event.key == K_LEFT:
                olive.direction = 'L'
            if event.key == K_UP:
                olive.direction = 'U'
            if event.key == K_DOWN:
                olive.direction = 'D'

        if event.type == TICK and snakeMove:
          # Move every TICK milli second
          olive.move()
          # Update.
          if olive.munched(snack):
            olive.grow = True
            score += 1
            snack.teleport()

          if olive.ifTouchingEdge(screen):
            gameState = 'Over'

          if olive.ifTouchingSelf():
            gameState = 'Over'

      # Draw.
      displayScore()
      olive.draw(screen)
      snack.draw(screen)
      
      pygame.display.flip()
      fpsClock.tick(fps)

    elif gameState == 'Over':
      screen.fill(('BLACK'))

      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
          score = 0
          snakeMove = False
          olive.reset(GRIDSIZE)
          gameState = 'Play'

      # Draw
      # Display Game Over
      font = pygame.font.Font(None, 60)
      message_surface = font.render("Game Over", True, (255, 255, 255))
      x_position = width/2 - message_surface.get_width()/2
      y_position = height/2 - message_surface.get_height()/2
      screen.blit(message_surface, (x_position, y_position))

      # Display Replay instruction
      font = pygame.font.Font(None, 25)
      message_surface = font.render("(Press SPACE to Replay)", True, (255, 255, 255))
      offset = 45
      x_position = width/2 - message_surface.get_width()/2
      y_position = height/2 - message_surface.get_height()/2 + offset
      screen.blit(message_surface, (x_position, y_position))    

      pygame.display.flip()
      fpsClock.tick(fps)

gameOn()