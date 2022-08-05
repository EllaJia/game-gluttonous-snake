import pygame
import sys
import random
from pygame.locals import *

class Snake(object):
    # produce background and snake
    def __init__(self):
        self.black = pygame.Color(0, 0, 0)
        self.red = pygame.Color(255, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        
    def gameover(self):
        pygame.quit()
        sys.exit()
    
    def initialize(self):
        pygame.init()
        clock = pygame.time.Clock()
        playSurface = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Python gluttonous snake mini game')
        snakePosition = [80, 80]
        snakebody = [[80, 80], [60, 80], [40, 80]]
        targetPosition = [200,400]
        targetflag = 1 # whether the fruit has been eaten
        direction = 'right'
        changeDirection = direction
        self.main(snakebody, targetPosition, targetflag, direction, changeDirection, snakePosition, playSurface, clock)
        
    def main(self, snakebody, targetPosition, targetflag, direction, changeDirection, snakePosition, playSurface, clock):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        changeDirection = 'right'
                        print('')
                    if event.key == K_LEFT:
                        changeDirection = 'left'
                        print('')
                    if event.key == K_DOWN:
                        changeDirection = 'down'
                        print('')
                    if event.key == K_UP:
                        changeDirection = 'up'
                        print('')
                    if event.key == K_ESCAPE:
                        pygame.event.post(pygame.event.Event(QUIT))
            
            if changeDirection == 'left' and not direction == 'right':
                direction = changeDirection
            if changeDirection == 'right' and not direction == 'left':
                direction = changeDirection
            if changeDirection == 'down' and not direction == 'up':
                direction = changeDirection
            if changeDirection == 'up' and not direction == 'down':
                direction = changeDirection
            
            if direction == 'right':
                snakePosition[0] += 20
            if direction == 'left':
                snakePosition[0] -= 20
            if direction == 'up':
                snakePosition[1] -= 20
            if direction == 'down':
                snakePosition[1] += 20
                
            snakebody.insert(0, list(snakePosition))
            if snakePosition[0] == targetPosition[0] and snakePosition[1] == targetPosition[1]:
                targetflag = 0
            else:
                snakebody.pop()
                
            if targetflag == 0:
                x = random.randrange(1, 40)
                y = random.randrange(1, 30)
                targetPosition = [int(x * 20), int(y * 20)]
                targetflag = 1
                
            playSurface.fill(self.black)
            for position in snakebody:
                pygame.draw.rect(playSurface, self.white, Rect(position[0], position[1], 20, 20))
                pygame.draw.rect(playSurface, self.red, Rect(targetPosition[0], targetPosition[1], 20, 20))
                
            pygame.display.flip()
            
            if snakePosition[0] > 900 or snakePosition[0] < 0:
                snake.gameover()
            elif snakePosition[1] > 800 or snakePosition[1] < 0:
                snake.gameover()
            for i in snakebody[1:]:
                if snakePosition[0] == i[0] and snakePosition[1] == i[1]:
                    snake.gameover()
                    
            clock.tick(5)

snake = Snake()
snake.initialize()