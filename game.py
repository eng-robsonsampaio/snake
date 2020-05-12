import sys
import json
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
pygame.init()
screen_game = pygame.display.set_mode((screen_size, screen_size))

snake = Snake(automatic=False)

apple = Apple(screen_size)
apple.set_random_position(screen_size)

my_direction  = RIGHT
clock = pygame.time.Clock()

def read_score():
    with open("highscore.json", "r") as file:
        return json.loads(file.read())

def save_score():
    with open("highscore.json", "w") as file:
        json.dump(highscore_json, file, indent = 4, sort_keys=True)

def score(score):
    font = pygame.font.SysFont("comicsansms", 24)
    text = font.render("Score: "+str(score), True, (0, 128, 0))
    screen_game.blit(text, (20,5))

def highscore(highscore):
    font = pygame.font.SysFont("comicsansms", 24)
    text = font.render("Highscore: "+str(highscore), True, (0, 128, 0))
    screen_game.blit(text, (200,5))

def pause_game(paused):
    """
    Press SPACE to pause and again to continue
    """
    while paused:
        for event in pygame.event.get():
            if pygame.key.get_focused() and pygame.key.get_pressed()[K_SPACE]:
                paused = False


start_time = pygame.time.get_ticks()
start = datetime.now().replace(microsecond=0)
highscore_json = read_score()
apple_time = pygame.time.get_ticks()
while game_on:
    clock.tick(DELAY)

    snake.crawl()
    snake.avoid_the_wall(screen_size)

    if start_time + 500 < pygame.time.get_ticks():
        snake.random_crawl()
        start_time = pygame.time.get_ticks()
    

    for event in pygame.event.get():
        game_on = snake.handle_event(event)
        if event.type == KEYDOWN and event.key == K_SPACE:
            pause_game(True)


    if snake.hit_the_wall(screen_size) or snake.tail_collision(): game_on = False 
    
    if snake.eat_apple(apple.position):
        apple.set_random_position(screen_size)
        apple_time = pygame.time.get_ticks()
        snake.snake_bigger()
        DELAY += 0.5
        points += 1
    
    if apple_time + 4000 < pygame.time.get_ticks():
        apple.set_random_position(screen_size)
        apple_time = pygame.time.get_ticks()
    
    
    screen_game.fill((30,30,30))
    score(points)
    highscore(highscore_json["highscore"])
    screen_game.blit(apple.surface, apple.position)

    for snake_pos in snake.snake:
        screen_game.blit(snake.skin, snake_pos)
        
    pygame.display.update()
pygame.quit()
print("Game over")
print("Scores: "+str(points))
if points > highscore_json["highscore"]:
    highscore_json["highscore"] = points
    save_score()
print(f'\nElapsed time: {datetime.now().replace(microsecond=0) - start}')