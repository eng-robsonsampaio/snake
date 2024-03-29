import pygame
import sys
from game import run_game

# Pygame initialization
pygame.init()

# Set the dimensions of the screen
width = 800
height = 600
game_screen_width = 700
game_screen_height = 400

# Definição das cores
white = (255, 255, 255)
black = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Login')

# This is where the game will be played
game_screen = pygame.Surface((game_screen_width, game_screen_height))

# Set the window title
pygame.display.set_caption("Snake Game")

# Load background image
background_image = pygame.image.load("images/background_image.jpg")
background_image = pygame.transform.scale(background_image, (width, height))

# Define colors
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 200, 0)

# Define fonts
font_large = pygame.font.Font(None, 48)
font_small = pygame.font.Font(None, 24)
log_font = pygame.font.Font(None, 32)

# Define start button dimensions
button_width = 200
button_height = 50

# Calculate button position
button_x = (width - button_width) // 2
button_y = (height - button_height) // 2

# Define game states
START_SCREEN = 0
GAME_SCREEN = 1

# Load snake image
snake_image = pygame.image.load("images/snake.png")
snake_image = pygame.transform.scale(snake_image, (200, 200))

# Load apple image
apple_image = pygame.image.load("images/apple.png")
apple_image = pygame.transform.scale(apple_image, (50, 50))

# Initial game state
current_state = START_SCREEN

# Variable to track hover state
hovering = False

# Game screen position
game_screen_x = (width - game_screen_width) // 2
game_screen_y = (height - game_screen_height) // 2

# Game screen surface
game_screen_surface = pygame.Surface((game_screen_width, game_screen_height))

# Variável para armazenar o nome de usuário
username = ''

# Main game loop
game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_state == START_SCREEN:
                # Check if the mouse click is within the start button boundaries
                if button_x < event.pos[0] < button_x + button_width and button_y < event.pos[1] < button_y + button_height:
                    # Transition to the game screen
                    current_state = GAME_SCREEN
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                # Remove o último caractere do nome de usuário
                username = username[:-1]
            elif event.key == pygame.K_RETURN:
                # Faz algo com o nome de usuário digitado, como verificar a autenticação
                print("Nome de usuário:", username)
            else:
                # Adiciona o caractere digitado ao nome de usuário
                username += event.unicode

    # Fill the screen with the background image
    screen.blit(background_image, (0, 0))
    
    if current_state == START_SCREEN:
        # Check if the mouse is hovering over the start button
        if button_x < pygame.mouse.get_pos()[0] < button_x + button_width and button_y < pygame.mouse.get_pos()[1] < button_y + button_height:
            hovering = True
        else:
            hovering = False

        # Draw the start button
        if hovering:
            pygame.draw.rect(screen, LIGHT_GREEN, (button_x, button_y, button_width, button_height))
        else:
            pygame.draw.rect(screen, GREEN, (button_x, button_y, button_width, button_height))

        start_text = font_small.render("START", True, (0, 0, 0))
        text_rect = start_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(start_text, text_rect)

        # Draw the "Welcome" message
        welcome_text = font_large.render("Welcome to Snake Game!", True, (0, 0, 0))
        welcome_rect = welcome_text.get_rect(center=(width // 2, height // 3))
        screen.blit(welcome_text, welcome_rect)

        # Draw the snake image
        snake_rect = snake_image.get_rect(center=(width // 2 + 150, height // 2 + 200))
        screen.blit(snake_image, snake_rect)

        # Draw the apple image
        apple_rect = apple_image.get_rect(center=(width // 2 - 150, height - 500))
        screen.blit(apple_image, apple_rect)

    elif current_state == GAME_SCREEN:
        # Fill the game screen with a solid color
        game_screen_surface.fill((255, 255, 255))
        
         # Call the game function to run the snake game on the game screen surface
        if (run_game(screen, game_screen_surface) == True):
            break
        # Draw the game screen surface on the main screen
        # screen.blit(game_screen_surface, (game_screen_x, game_screen_y))
        

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
