def run_game(screen_game, game_screen_surface):
    import sys
    import json
    import pygame
    import random
    from datetime import datetime
    from pygame.locals import pygame
    from apple import Apple
    from snake import Snake
    from settings import HS_FILE
    from os import path 
    

    RIGHT = 3
    DELAY = 10
    points = 0
    screen_size = 700
    screen_score = (screen_size, 30)
    game_on =  True
    paused = False

    # screen_game = pygame.display.set_mode((screen_size, screen_size+50))
    board = pygame.Surface(screen_score)
    board.fill((180, 180, 180))


    snake = Snake(automatic=False)

    apple = Apple(screen_size)
    apple.set_random_position(screen_size)

    my_direction  = RIGHT
    clock = pygame.time.Clock()



    def read_score():
        with open("record.json", "r") as file:
            return json.loads(file.read())

    def save_score():
        with open("record.json", "w") as file:
            json.dump(record_json, file, indent = 4, sort_keys=True)

    def score(score):
        font = pygame.font.SysFont("comicsansms", 24)
        text = font.render("Score: "+str(score), True, (0, 60, 30))
        screen_game.blit(text, (50,0))

    def print_record(score_record):
        font = pygame.font.SysFont("comicsansms", 24)
        text = font.render("Record: "+str(score_record), True, (0, 60, 30))
        screen_game.blit(text, (600,0))

    def pause_game(paused):
        """
        Press SPACE to pause and again to continue
        """
        while paused:
            print("inside while")
            for event in pygame.event.get():
                print("inside for")
                if pygame.key.get_focused() and pygame.key.get_pressed()[pygame.K_SPACE]:
                    print("inside if")
                    paused = False


    start_time = pygame.time.get_ticks()
    start = datetime.now().replace(microsecond=0)
    record_json = read_score()
    apple_time = pygame.time.get_ticks()

    while game_on:
        clock.tick(DELAY)

        snake.crawl()
        # snake.avoid_the_wall(screen_size)

        if start_time + 500 < pygame.time.get_ticks():
            snake.random_crawl()
            start_time = pygame.time.get_ticks()

        event = pygame.event.get()
        if event: 
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                pause_game(True)
            else :
                game_on = snake.handle_event(event[0])

        if snake.hit_the_wall(screen_size) or snake.tail_collision(): 
            print(snake.get_position())
            game_on = False 
        
        if snake.eat_apple(apple.position):
            apple.set_random_position(screen_size)
            apple_time = pygame.time.get_ticks()
            snake.snake_bigger()
            DELAY += 0.5
            points += 1
        
        #Estou acelerando o tempo que a maça aparece
        if apple_time + 4500 < pygame.time.get_ticks():
            apple.set_random_position(screen_size)
            apple_time = pygame.time.get_ticks()
        
        width, height = game_screen_surface.get_size()
        rect = pygame.Rect(50, 100, width, height)  # X, Y, largura, altura
        screen_game.fill((50,80,80), rect)
        screen_game.blit(board, (50,0))
        score(points)
        print_record(record_json["record"])
        screen_game.blit(apple.surface, apple.position)

        for snake_pos in snake.snake[:-1]:
            screen_game.blit(snake.skin, snake_pos)

        screen_game.blit(snake.head, snake.snake[-1]) 
            
        pygame.display.update()
    

    print("Game over")
    print("Scores: "+str(points))
    if points > record_json["record"]:
        record_json["record"] = points
        save_score()
    print(f'\nElapsed time: {datetime.now().replace(microsecond=0) - start}')
    return True
