import pygame
import random
from time import sleep
from pygame.locals import *

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
delay = 0.05
pygame.init()
screen = pygame.display.set_mode((600, 600))
game_on =  True

# snake = [(x, y)]
snake = [(200, 200), (210, 200), (220, 200), (230, 200), (240, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

apple = pygame.Surface((10,10))
apple.fill((255,0,0))
apple_pos = (random.randint(0, 590), random.randint(0, 590))

my_direction  = RIGHT

while game_on:

    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key==K_UP:
                my_direction = UP
                print("UP")
            elif event.key==K_LEFT:
                my_direction = LEFT
                print("LEFT")
            elif event.key==K_DOWN:
                my_direction = DOWN
                print("DOWN")
            elif event.key==K_RIGHT:
                my_direction = RIGHT
                print("RIGHT")

    if snake[len(snake)-1][0] == 600 or snake[len(snake)-1][0] == -10 or snake[len(snake)-1][1] == 600 or snake[len(snake)-1][1] == -10:
        print("Game over")
    # [( x, y )]
    # (200, 200), (210, 200), (220, 200), (230, 200), (240, 200)]
    if my_direction == RIGHT:
        sleep(delay)
        snake.append((snake[len(snake)-1][0] + 10 , snake[len(snake)-1][1]))
        snake.pop(0)
    elif my_direction == UP:
        sleep(delay)
        snake.append((snake[len(snake)-1][0] , snake[len(snake)-1][1] - 10))
        snake.pop(0)
    elif my_direction == DOWN:
        sleep(delay)
        snake.append((snake[len(snake)-1][0] , snake[len(snake)-1][1] + 10))
        snake.pop(0)
    elif my_direction == LEFT:        
        sleep(delay)
        snake.append((snake[len(snake)-1][0] - 10 , snake[len(snake)-1][1]))
        snake.pop(0)
    
    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for snake_pos in snake:
        screen.blit(snake_skin, snake_pos)

    pygame.display.update()