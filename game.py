import pygame
import random
from pygame.locals import *
from apple import *
from snake import *

"""
Constants
"""
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
DELAY = 10

pygame.init()
screen_size = 400
screen_game = pygame.display.set_mode((screen_size, screen_size))
game_on =  True

snake = Snake()

apple = Apple(screen_size)
apple.set_random_position(screen_size)

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
        game_on = snake.handle_event(event)
        if event.type == KEYDOWN and event.key==K_SPACE:
            pause_game(True)


    if snake.hit_the_wall(screen_size):
        game_on = False
    
    if snake.eat_apple(apple.position):
        apple.set_random_position(screen_size)
        snake.snake_bigger()
        DELAY += 0.5
        points += 1
    
    if snake.tail_collision():
        print(snake.snake)
        print("Tails collision")
        game_on = False

    snake.crawl()
    
    screen_game.fill((30,30,30))
    score(points)
    screen_game.blit(apple.surface, apple.position)

    for snake_pos in snake.snake:
        screen_game.blit(snake.skin, snake_pos)
        
    pygame.display.update()
pygame.quit()
print("Game over")