import pygame
import random
from pygame.locals import *

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
delay = 0.05
pygame.init()
screen = pygame.display.set_mode((600, 600))
game_on =  True

# snake = [(x, y),   (x+n, y),   (x+2n, y)]
snake = [(200, 200), (210, 200), (220, 200), (230, 200), (240, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

# apple
apple = pygame.Surface((10,10))
apple.fill((255,0,0))
apple_pos = (random.randrange(0, 590, 10), random.randrange(0, 590, 10))
# apple_pos = ((300, 200))

my_direction  = RIGHT

clock = pygame.time.Clock()

def collision(pos1, pos2):
    # return (pos1[0] == pos2[0] and pos1[1] == pos2[1])
    return pos1 == pos2

def snake_tail_collision(head, tail):
    return (head in tail)

while game_on:
    clock.tick(20)
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            game_on = False
        if event.type == KEYDOWN:
            if event.key==K_UP and my_direction != DOWN:
                my_direction = UP
                print("UP")
            elif event.key==K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
                print("LEFT")
            elif event.key==K_DOWN and my_direction != UP:
                my_direction = DOWN
                print("DOWN")
            elif event.key==K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
                print("RIGHT")

    if snake[len(snake)-1][0] == 600 or snake[len(snake)-1][0] == -10 or snake[len(snake)-1][1] == 600 or snake[len(snake)-1][1] == -10:
        print("Game over")
        pygame.quit()
        game_on = False
    
    if collision(snake[len(snake)-1], apple_pos):
        apple_pos = (random.randrange(0, 590, 10), random.randrange(0, 590, 10))
        snake.insert(0,(0,0))
    
    if snake_tail_collision(snake[len(snake)-1], snake[0:len(snake)-2]):
        print("Game over")
        pygame.quit()
        game_on = False

    # [( x, y )]
    # (200, 200), (210, 200), (220, 200), (230, 200), (240, 200)]
    if my_direction == RIGHT:
        snake.append((snake[len(snake)-1][0] + 10 , snake[len(snake)-1][1]))
        snake.pop(0)
    elif my_direction == UP:
        snake.append((snake[len(snake)-1][0] , snake[len(snake)-1][1] - 10))
        snake.pop(0)
    elif my_direction == DOWN:
        snake.append((snake[len(snake)-1][0] , snake[len(snake)-1][1] + 10))
        snake.pop(0)
    elif my_direction == LEFT:        
        snake.append((snake[len(snake)-1][0] - 10 , snake[len(snake)-1][1]))
        snake.pop(0)
    
    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for snake_pos in snake:
        screen.blit(snake_skin, snake_pos)

    pygame.display.update()