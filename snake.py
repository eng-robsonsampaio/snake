import pygame
import random
from pygame.locals import *
from datetime import datetime

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

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

    def avoid_the_wall(self, screen_size):
        dist = 30
        if self.automatic:
            if self.my_direction == LEFT and self.snake[self.lenght-1][0] - dist <= 0 or self.my_direction == RIGHT and self.snake[self.lenght-1][0] + dist >= screen_size:
                self.automatic = False
                print(f"Automatic UP DOWN: {self.automatic}")
                print(f"({self.snake[self.lenght-1][0]}, {self.snake[self.lenght-1][1]})")
                if self.snake[self.lenght-1][1] >= screen_size/2:
                    self.my_direction = UP
                elif self.snake[self.lenght-1][1] < screen_size/2:
                    self.my_direction = DOWN
                # else:                    
                #     self.my_direction = [UP, DOWN][random.randint(0,1)]
                #     print(f"Manual random: [UP, DOWN] {self.my_direction}")
            if self.my_direction == UP and self.snake[self.lenght-1][1] - dist <= 0 or self.my_direction == DOWN and self.snake[self.lenght-1][1] + dist >= screen_size:
                self.automatic = False
                print(f"Automatic LEFT RIGHT: {self.automatic}")
                print(f"({self.snake[self.lenght-1][0]}, {self.snake[self.lenght-1][1]})")
                if self.snake[self.lenght-1][0] >= screen_size/2:
                    self.my_direction = LEFT
                elif self.snake[self.lenght-1][0] < screen_size/2:
                    self.my_direction = RIGHT
                # else:
                #     self.my_direction = [RIGHT, LEFT][random.randint(0,1)]
                #     print(f"Manual random: [LEFT, RIGHT] {self.my_direction}")
            self.automatic = True


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
        # collision = self.snake[self.lenght-1] in self.snake[0:self.lenght-3]
        for pos in self.snake[:-2]:
            if pos == self.snake[-1]:
                print("Tail collision")
                print(self.snake)
                print(f"Head: {self.snake[self.lenght-1]}")
                print(f"Tail: {self.snake[0:self.lenght-2]}")
                return True
        # else: 
        #     return False
        # if collision:
        #     print("Tail collision")
        #     print(self.snake)
        #     print(f"Head: {self.snake[self.lenght-1]}")
        #     print(f"Tail: {self.snake[0:self.lenght-2]}")
        #     print(f"Collision: {collision}")
        #     return True
        # else: 
        #     return False

    def crawl(self):
        if self.my_direction == RIGHT:
            self.snake.append((self.snake[self.lenght-1][0] + 10 , self.snake[self.lenght-1][1]))
        elif self.my_direction == UP:
            self.snake.append((self.snake[self.lenght-1][0] , self.snake[self.lenght-1][1]- 10))
        elif self.my_direction == DOWN:
            self.snake.append((self.snake[self.lenght-1][0] , self.snake[self.lenght-1][1]+ 10))
        elif self.my_direction == LEFT:        
            self.snake.append((self.snake[self.lenght-1][0] - 10 , self.snake[self.lenght-1][1]))
        self.snake.pop(0)
        
        

    def handle_event(self, event):
        if event.type == QUIT:
            return False
        if event.type == KEYDOWN:
            if event.key==K_UP and self.my_direction != DOWN:
                print("UP")
                self.my_direction = UP                
            elif event.key==K_LEFT and self.my_direction != RIGHT:
                print("LEFT")
                self.my_direction = LEFT                
            elif event.key==K_DOWN and self.my_direction != UP:
                print("DOWN")
                self.my_direction = DOWN                
            elif event.key==K_RIGHT and self.my_direction != LEFT:
                print("RIGHT")
                self.my_direction = RIGHT                
        return True