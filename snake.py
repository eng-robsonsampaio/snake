import pygame
import random
from pygame.locals import *

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
DELAY = 10
pygame.init()
sreen_size = 400
screen_game = pygame.display.set_mode((sreen_size, sreen_size))
game_on =  True

# snake = [(x, y),   (x+n, y),   (x+2n, y)]
snake = [(200, 200), (210, 200), (220, 200), (230, 200), (240, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

# apple
apple = pygame.Surface((10,10))
apple.fill((255,0,0))
apple_pos = (random.randrange(0, sreen_size-10, 10), random.randrange(0, sreen_size-10, 10))

points = 0

def score(score):
    font = pygame.font.SysFont("comicsansms", 24)
    text = font.render("Score: "+str(score), True, (0, 128, 0))
    screen_game.blit(text, (20,5))

my_direction  = RIGHT
clock = pygame.time.Clock()

def grabing_apple(pos1, pos2):
    return pos1 == pos2

def snake_tail_collision(head, tail):
    return (head in tail)

paused = False
def pause_game(paused):
    """
    Press SPACE to pause and again to continue
    """
    while paused:
        for event in pygame.event.get():
            if pygame.key.get_focused() and pygame.key.get_pressed()[K_SPACE]:
                paused = False


while game_on:
    clock.tick(DELAY)
    # pressed = pygame.key.get_pressed()
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
            elif pygame.key.get_focused() and pygame.key.get_pressed()[K_SPACE]:
                pause_game(True)
                # print("Press space to continue")

    # while paused:
    #     for event in pygame.event.get():
    #         if pygame.key.get_focused() and pygame.key.get_pressed()[K_SPACE]:
    #             paused = False

    if snake[len(snake)-1][0] == sreen_size or snake[len(snake)-1][0] == -10 or snake[len(snake)-1][1] == sreen_size or snake[len(snake)-1][1] == -10:
        print("Game over")
        pygame.quit()
        game_on = False
    
    if grabing_apple(snake[len(snake)-1], apple_pos):
        apple_pos = (random.randrange(0, sreen_size-10, 10), random.randrange(0, sreen_size-10, 10))
        snake.insert(0,(0,0))
        DELAY += 0.5
        points += 1
    
    if snake_tail_collision(snake[len(snake)-1], snake[0:len(snake)-2]):
        print("Tails collision")
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
    
    screen_game.fill((30,30,30))
    score(points)
    screen_game.blit(apple, apple_pos)
    for snake_pos in snake:
        screen_game.blit(snake_skin, snake_pos)
        
    pygame.display.update()