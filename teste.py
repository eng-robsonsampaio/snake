import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definição das dimensões da janela
window_width = 800
window_height = 600

# Definição das cores
white = (255, 255, 255)
black = (0, 0, 0)

# Criação da janela
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Login')

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

    # Limpa a janela
    window.fill(white)

    # Desenha o campo de entrada do nome de usuário
    pygame.draw.rect(window, black, (300, 200, 200, 40))
    pygame.draw.rect(window, white, (305, 205, 190, 30))

    # Desenha o texto digitado pelo usuário
    text_surface = font.render(username, True, black)
    window.blit(text_surface, (310, 210))

    # Atualiza a tela
    pygame.display.flip()
