import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definição das dimensões da janela
window_width = 800
window_height = 600

# Criação da janela
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Login')

# Carregamento do background image
background_image = pygame.image.load("images/background_image.jpg")

# Definição das cores
white = (255, 255, 255)
black = (0, 0, 0)

# Definição das fontes
font = pygame.font.Font(None, 32)

# Variável para armazenar o nome de usuário
username = ''

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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

    # Blit do background image na tela principal
    window.blit(background_image, (0, 0))

    # Criação de uma nova superfície para o campo de entrada do nome de usuário
    input_surface = pygame.Surface((200, 40))
    input_surface.fill(white)
    input_surface.set_alpha(200)  # Define a transparência da superfície
    input_rect = input_surface.get_rect()
    input_rect.center = (window_width // 2, window_height // 3)  # Centraliza o campo de entrada

    # Desenha o campo de entrada do nome de usuário na nova superfície
    pygame.draw.rect(input_surface, black, (5, 5, 190, 30))
    pygame.draw.rect(input_surface, white, (10, 10, 180, 20))

    # Desenha o texto digitado pelo usuário na nova superfície
    text_surface = font.render(username, True, black)
    input_surface.blit(text_surface, (15, 15))

    # Blit da nova superfície sobre a tela principal
    window.blit(input_surface, input_rect)

    # Atualiza a tela
    pygame.display.flip()
