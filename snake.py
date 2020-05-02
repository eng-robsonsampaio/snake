import pygame
import random
from pygame.locals import *

class Snake():

    def __init__(self, lenght=5):
        """
        height: y height
        """
        self.lenght = lenght
        self.snake = [(240, 200), (230, 200), (220, 200), (210, 200), (200, 200)]
        self.snake_skin = pygame.Surface((10, 10)).fill((255, 255, 255))

    def snake_walk(self):
        self.snake.append((0,0))
        self.lenght += 1
        self.snake.pop()

    def collision(self):
        return self.snake[0] in self.snake[1:self.lenght-1]
    
    def snake_hit_the_wall(self, wall):
        return self.snake in wall


class Screen:

    def __init__(self, height, lenght):
        """
        height: y height
        lenght: x lenght
        """
        self.screen_size  = (height, lenght)
        self.screen = pygame.display.set_mode(self.screen_size)

class Apple:

    def __init__(self, height, lenght, screen_size):
        """
        height: y height
        lenght: x lenght
        """
        self.height = height
        self.lenght = lenght
        self.screen_size = screen_size
        self.apple_size = (height, lenght)
        self.apple = pygame.Surface(self.apple_size).fill((255, 0, 0)) 

    def set_apple_position(self):
        return (random.randrange(0, self.screen_size[1]-self.lenght, self.lenght), random.randrange(0, self.screen_size[1]-self.lenght, self.lenght))


UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
DELAY = 10

pygame.init()
screen = pygame.display.set_mode((600, 600))
game_on =  True

# snake = [(x, y),   (x+n, y),   (x+2n, y)]
# snake = Snake()
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

def grabing_apple(pos1, pos2):
    return pos1 == pos2

def snake_tail_collision(head, tail):
    return (head in tail)

while game_on:
    clock.tick(DELAY)
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
    
    if grabing_apple(snake[len(snake)-1], apple_pos):
        apple_pos = (random.randrange(0, 590, 10), random.randrange(0, 590, 10))
        snake.insert(0,(0,0))
        DELAY += 1
    
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