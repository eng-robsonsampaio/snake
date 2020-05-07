import pygame
import random
from pygame.locals import *
from datetime import datetime

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
[UP, LEFT, RIGHT]
[DOWN, LEFT, RIGHT]
[RIGHT, UP, DOWN]
[LEFT, UP, DOWN]

class Snake:

    def __init__(self, size=(10, 10), color=(255, 255, 255), automatic=False):
        print("Creating Snake")
        self.snake = [(200, 200), (210, 200), (220, 200), (230, 200), (240, 200)]
        self.skin = pygame.Surface(size)
        self.skin.fill(color)
        self.lenght = 5
        self.my_direction = RIGHT
        self.automatic = automatic
        self.random_crawl()
    
    def random_crawl(self):        
        if self.automatic == True:
            print(f"Automatic: {self.automatic}")
            if self.my_direction == UP:
                self.my_direction = [UP, LEFT, RIGHT][random.randint(0,2)]
            elif self.my_direction == DOWN:
                self.my_direction = [DOWN, LEFT, RIGHT][random.randint(0,2)]
            elif self.my_direction == LEFT:
                self.my_direction = [LEFT, UP, DOWN][random.randint(0,2)]
            else:
                self.my_direction = [RIGHT, UP, DOWN][random.randint(0,2)]

    def back_to_automatic(self, screen_size):
        if self.automatic == False and self.hit_the_wall(screen_size):
            self.automatic = True

    
    def avoid_the_wall(self, screen_size):
        x = self.snake[self.lenght-1][0]
        y = self.snake[self.lenght-1][1]
        dist = 10
        if self.automatic:
            if self.my_direction == LEFT and x - dist < 0 or self.my_direction == RIGHT and x + dist >= screen_size:
                self.automatic = 0
                print(f"Automatic: {self.automatic}")
                if y + dist >= screen_size:
                    self.my_direction = UP
                elif y - dist <= 0:
                    self.my_direction = DOWN
                else:                    
                    self.my_direction = [UP, DOWN][random.randint(0,1)]
                    print(f"Manual random: [UP, DOWN] {self.my_direction}")
            elif self.my_direction == UP and y - dist < 0 or self.my_direction == DOWN and y + dist >= screen_size:
                self.automatic = 0
                print(f"Automatic: {self.automatic}")
                if x + dist >= screen_size:
                    self.my_direction = LEFT
                elif x - dist <= 0:
                    self.my_direction = RIGHT
                else:
                    self.my_direction = [RIGHT, LEFT][random.randint(0,1)]
                    print(f"Manual random: [UP, DOWN] {self.my_direction}")
            # self.automatic = 1


    def get_position(self):
        return self.snake

    def hit_the_wall(self, screen_size):
        if self.snake[self.lenght-1][0] >= screen_size or self.snake[self.lenght-1][0] < 0 or self.snake[self.lenght-1][1] >= screen_size or self.snake[self.lenght-1][1] < 0:
            print(self.snake)
            return True
        else:
            return False

    def eat_apple(self, apple_pos):
        return self.snake[self.lenght-1] == apple_pos
    
    def snake_bigger(self):
        self.snake.insert(0,(self.snake[0][0],self.snake[1][1]))
        self.lenght += 1
    
    def tail_collision(self):
        collision = self.snake[self.lenght-1] in self.snake[0:self.lenght-3]
        if collision:
            print(self.snake)
            print(f"Head: {self.snake[self.lenght-1]}")
            print(f"Tail: {self.snake[0:self.lenght-2]}")
            print(f"Collision: {collision}")
            return True
        else: 
            return False

    def crawl(self):
        x = self.snake[self.lenght-1][0]
        y = self.snake[self.lenght-1][1]
        if self.my_direction == RIGHT:
            self.snake.append((x + 10 , y))
            self.snake.pop(0)
        elif self.my_direction == UP:
            self.snake.append((x , y - 10))
            self.snake.pop(0)
        elif self.my_direction == DOWN:
            self.snake.append((x , y + 10))
            self.snake.pop(0)
        elif self.my_direction == LEFT:        
            self.snake.append((x - 10 , y))
            self.snake.pop(0)
        
        

    def handle_event(self, event):
        if event.type == QUIT:
            return False
        if event.type == KEYDOWN:
            if pygame.key.get_focused() and event.key==K_UP and self.my_direction != DOWN:
                print("UP")
                self.my_direction = UP                
            elif pygame.key.get_focused() and event.key==K_LEFT and self.my_direction != RIGHT:
                print("LEFT")
                self.my_direction = LEFT                
            elif pygame.key.get_focused() and event.key==K_DOWN and self.my_direction != UP:
                print("DOWN")
                self.my_direction = DOWN                
            elif pygame.key.get_focused() and event.key==K_RIGHT and self.my_direction != LEFT:
                print("RIGHT")
                self.my_direction = RIGHT                
        return True