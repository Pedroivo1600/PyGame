import pygame

pygame.init()

WIDTH = 500
HEIGHT = 400
ball_width = 30
ball_height = 20
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Goalkeeper pro')
background = pygame.image.load('img/estádio.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
football = pygame.image.load('img/football.png').convert()
football = pygame.transform.scale(football, (ball_width, ball_height))


football_x = 250
football_y = -ball_height
football_speedx = 4
football_speedy = 8


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    football_x+=football_speedx
    football_y+=football_speedy
    if football_x > WIDTH or football_y > HEIGHT:
        football_x = 250
        football_y = -ball_height

        

    window.fill((255, 255, 255))
    window.blit(background, (0, 0))
    window.blit(football, (football_x, football_y))

    pygame.display.update()

pygame.quit()