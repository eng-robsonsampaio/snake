import pygame
import random
from pygame.locals import *

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
DELAY = 10

class Snake:

    def __init__(self, size=(10, 10), color=(255, 255, 255)):
        print("Creating Snake")
        self.snake = [(200, 200), (210, 200), (220, 200), (230, 200), (240, 200)]
        self.skin = pygame.Surface(size)
        self.skin.fill(color)
        self.lenght = 5
        self.my_direction = RIGHT

    def get_position(self):
        return self.snake

    def hit_the_wall(self, screen_size):
        return self.snake[self.lenght-1][0] == screen_size or self.snake[self.lenght-1][0] == -10 or self.snake[self.lenght-1][1] == screen_size or self.snake[self.lenght-1][1] == -10

    def eat_apple(self, apple_pos):
        return self.snake[self.lenght-1] == apple_pos
    
    def snake_bigger(self):
        self.snake.insert(0,(self.snake[0][0],self.snake[1][1]))
        self.lenght += 1
    
    def tail_collision(self):
        return self.snake[self.lenght-1] in self.snake[0:self.lenght-2]

    def crawl(self):
        if self.my_direction == RIGHT:
            self.snake.append((self.snake[self.lenght-1][0] + 10 , self.snake[self.lenght-1][1]))
            self.snake.pop(0)
        elif self.my_direction == UP:
            self.snake.append((self.snake[self.lenght-1][0] , self.snake[self.lenght-1][1] - 10))
            self.snake.pop(0)
        elif self.my_direction == DOWN:
            self.snake.append((self.snake[self.lenght-1][0] , self.snake[self.lenght-1][1] + 10))
            self.snake.pop(0)
        elif self.my_direction == LEFT:        
            self.snake.append((self.snake[self.lenght-1][0] - 10 , self.snake[self.lenght-1][1]))
            self.snake.pop(0)
        
        

    def handle_event(self, event):
        if event.type == QUIT:
            return False
        if event.type == KEYDOWN:
            if pygame.key.get_focused() and event.key==K_UP and self.my_direction != DOWN:
                self.my_direction = UP
                print("UP")
            elif pygame.key.get_focused() and event.key==K_LEFT and self.my_direction != RIGHT:
                self.my_direction = LEFT
                print("LEFT")
            elif pygame.key.get_focused() and event.key==K_DOWN and self.my_direction != UP:
                self.my_direction = DOWN
                print("DOWN")
            elif pygame.key.get_focused() and event.key==K_RIGHT and self.my_direction != LEFT:
                self.my_direction = RIGHT
                print("RIGHT")
        return True