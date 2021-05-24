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


class Football(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        #Posição da bola
        self.rect.x = random.randint(250, WIDTH-ball_width)
        self.rect.y = random.randint(-50, -ball_height)
        #Velocidade da bola
        self.speed_football_speedx = random.randint(-2, 2)
        self.speed_football_speedy = random.randint(4, 6)
    
    def update(self):
        self.rect.x += self.speed_football_speedx
        self.rect.y += self.speed_football_speedy
        if self.rect.right > WIDTH or self.rect.top > HEIGHT:
            self.rect.x = random.randint(250, WIDTH-ball_width)
            self.rect.y = random.randint(-50, -ball_height)
            self.speed_football_speedx = random.randint(-2, 2)
            self.speed_football_speedy = random.randint(4, 6)







#Definindo os frames por segundo para ajustar a velocidade da bola
clock = pygame.time.Clock()
FPS = 30

all_balls = pygame.sprite.Group()
for i in range(5):
    balls = Football(football)
    all_balls.add(balls)


game = True
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    #controlando movimentos das 5 bolas no loop
    all_balls.update()
    
    #Adicionando imagens para tela principal
    window.fill((255, 255, 255))
    window.blit(background, (0, 0))
    all_balls.draw(window)

    pygame.display.update()

pygame.quit()