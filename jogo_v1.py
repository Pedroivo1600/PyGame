import pygame
import random
pygame.init()

#MEDIDAS
WIDTH = 500
HEIGHT = 400
ball_width = 30
ball_height = 20

#Defininindo a tela principal e imagens
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Goalkeeper pro')
background = pygame.image.load('img/estadio.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
football = pygame.image.load('img/football.png').convert_alpha()
football = pygame.transform.scale(football, (ball_width, ball_height))

#Posição da bola
football_x = random.randint(250, WIDTH-ball_width)
football_y = random.randint(-50, -ball_height)
#Velocidade da bola
football_speedx = random.randint(-2, 2)
football_speedy = random.randint(4, 6)

#Definindo os frames por segundo para ajustar a velocidade da bola
clock = pygame.time.Clock()
FPS = 30

game = True
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    football_x+=football_speedx
    football_y+=football_speedy
    if football_x > WIDTH or football_y > HEIGHT:
        football_x = random.randint(250, WIDTH-ball_width)
        football_y = random.randint(-50, -ball_height)
        football_speedx = random.randint(-2, 2)
        football_speedy = random.randint(4, 6)

    x = pygame.time.get_ticks()
    
    print(x)

        
    #Adicionando imagens para tela principal
    window.fill((255, 255, 255))
    window.blit(background, (0, 0))
    window.blit(football, (football_x, football_y))
    print(football_speedx)

    pygame.display.update()

pygame.quit()