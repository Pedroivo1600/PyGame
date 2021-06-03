import random
import pygame
from config import WIDTH, HEIGHT, list_lives, ball_width, ball_height
from assets import goal_sound

#======================
#-------Classes-------
#======================


#Goleiro
class Gk(pygame.sprite.Sprite):
    def __init__(self, img, golden_image):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
 
        self.image = img
        self.golden_image = golden_image
        self.regular_image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
 
    def update(self,shield):
        # Atualização da posição da nave
        self.rect.x += self.speedx
 
        # Mantem dentro da tela
        if shield:
            self.image = self.golden_image
        else:
            self.image = self.regular_image
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


#Bola de Futebol
class Football(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)
 
        self.image = img
        self.rect = self.image.get_rect()
        #Posição da bola
        self.rect.x = random.randint(250, WIDTH-ball_width)
        self.rect.y = random.randint(-50, -ball_height)
        #Velocidade da bola
        self.speed_football_speedx = random.randint(-2, 2)
        self.speed_football_speedy = random.randint(4, 6)
   
    #Atualização da posição da Bola de Futebol e outros
    def update(self,shield):

        #Atualização da posição da bola de futebol
        self.rect.x += self.speed_football_speedx
        self.rect.y += self.speed_football_speedy
        #Se o jogador pegar o powerup "Shield" durante o jogo ele não perde vida
        if self.rect.top > HEIGHT:
            if not shield:
                list_lives.append(1)
                goal_sound.play()
        #novas posições e velocidades
        if self.rect.right > WIDTH or self.rect.top > HEIGHT or self.rect.left < 0:
            self.rect.x = random.randint(250, WIDTH-ball_width)
            self.rect.y = random.randint(-50, -ball_height)
            self.speed_football_speedx = random.randint(-2, 2)
            self.speed_football_speedy = random.randint(4, 6)

#Powerup "Shield" 
class PowerUp(pygame.sprite.Sprite):
   
    # Construtor da classe.
    def __init__(self, img):

        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        #Posição do Shield
        self.rect.x = random.randint(250, WIDTH-100)
        self.rect.y = random.randint(-50, -ball_height)
        #Velocidade do shield
        self.speed_footbal_speedx = random.randint(-2, 2)
        self.speed_football_speedy = random.randint(4, 6)
    
    #Atualização na posição do "Power up" e outros
    def update(self,p_up):
        
        # Chama a variável "p_up" definida previamente (definida incialmente como "p_up = False")
        

        
        #Posição do power up quando ele está aparencendo no jogo
        print("if do update {0}".format(p_up))
        if p_up:
            self.rect.x += self.speed_footbal_speedx
            self.rect.y += self.speed_football_speedy
        
        #Ajusta a posição do powwerup caso sua posiçao esteja maior q a largura ou altura da tela do jogo
        if self.rect.right > WIDTH or self.rect.top > HEIGHT or self.rect.left < 0:
            self.rect.x = random.randint(250, WIDTH-100)
            self.rect.y = random.randint(-50, -ball_height)
            self.speed_football_speedx = random.randint(-2, 2)
            self.speed_football_speedy = random.randint(4, 6)
            p_up = False
        return(p_up)
    
    #Se o jogador colidir com o power up, o código abaixo faz com que o power up continue aparecendo
    def update_collide(self,p_up):
        if not p_up:
            self.rect.x = random.randint(250, WIDTH-100)
            self.rect.y = random.randint(-50, -ball_height)
            self.speed_football_speedx = random.randint(-2, 2)
            self.speed_football_speedy = random.randint(4, 6)