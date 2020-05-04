import sys
import pygame
import random
from pygame.locals import *
from apple import *
from snake import *
from settings import *
from os import path 


UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
DELAY = 10
points = 0
screen_size = 400
game_on =  True
paused = False
highscore = 0
pygame.init()
screen_game = pygame.display.set_mode((screen_size, screen_size))

snake = Snake()

apple = Apple(screen_size)
apple.set_random_position(screen_size)

my_direction  = RIGHT
clock = pygame.time.Clock()

def score(score):
    font = pygame.font.SysFont("comicsansms", 24)
    text = font.render("Score: "+str(score), True, (0, 128, 0))
    screen_game.blit(text, (20,5))

def read_high_score(highscore):
    with open("highscore.txt", "r") as file:
        highscore = file.read()
        font = pygame.font.SysFont("comicsansms", 24)
        text = font.render("High score: "+str(highscore), True, (0, 128, 0))
        screen_game.blit(text, (200,5))

def write_high_score(score):
    with open("highscore.txt", "w+") as file:
        print("Highscore: "+str(highscore))
        if int(highscore) < score: 
            print("escreve high score")
            file.write(str(score))

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

    snake.crawl()

    for event in pygame.event.get():
        game_on = snake.handle_event(event)
        if event.type == KEYDOWN and event.key == K_SPACE:
            pause_game(True)


    if snake.hit_the_wall(screen_size): game_on = False 
    
    if snake.tail_collision(): game_on = False
    
    if snake.eat_apple(apple.position):
        apple.set_random_position(screen_size)
        snake.snake_bigger()
        DELAY += 0.5
        points += 1
    
    screen_game.fill((30,30,30))
    score(points)
    read_high_score(highscore)
    screen_game.blit(apple.surface, apple.position)

    for snake_pos in snake.snake:
        screen_game.blit(snake.skin, snake_pos)
        
    pygame.display.update()
pygame.quit()
print("Game over")
print("Scores: "+str(points))
write_high_score(points)