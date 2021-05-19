import pygame

pygame.init()

WIDTH = 500
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Goalkeeper pro')
background = pygame.image.load('img/estádio.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.fill((255, 255, 255))
    window.blit(background, (0, 0))

    pygame.display.update()

pygame.quit()