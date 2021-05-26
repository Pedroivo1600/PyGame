import pygame
import random
pygame.init()
 
#MEDIDAS
 
#Medidas do background (estadio)
WIDTH = 500
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
 
#Medidas das bolas
ball_width = 30
ball_height = 20
 
#Medidas do goleiro
gk_width = 70
gk_height = 60
 
#Inicia assets
assets = {}
assets['background'] =  pygame.image.load('img/estadio.png').convert()
assets["background"] = pygame.transform.scale(assets["background"], (WIDTH, HEIGHT))
assets['football_img'] =  pygame.image.load('img/football.png').convert_alpha()
assets['football_img'] = pygame.transform.scale(assets["football_img"], (ball_width, ball_height))
assets['goalkeeper_img'] = pygame.image.load('img/Goalkeeper.png').convert_alpha()
assets['goalkeeper_img'] = pygame.transform.scale(assets["goalkeeper_img"], (gk_width, gk_height))
assets['powerup'] = pygame.image.load('img/powerup_shield.png').convert_alpha()
assets['powerup'] = pygame.transform.scale(assets['powerup'], (ball_width, ball_height))
 

salvou_anim = []
 

for i in range(9):
    # Os arquivos de animação são numerados de 00 a 08
    filename = 'img/salvada.png'.format(i)
    img = pygame.image.load(filename).convert()
    img = pygame.transform.scale(img, (32, 32))
    salvou_anim.append(img)
assets["salvou_anim"] = salvou_anim



class Gk(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
 
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
 
    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx
 
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
 
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
 

class Salvou(pygame.sprite.Sprite):
    def __init__(self, center, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
 
        # Armazena a animação de explosão
        self.salvou_anim = assets['salvou_anim']
 
        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.salvou_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem
 
        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()
 
        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50
 
    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update
 
        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now
 
            # Avança um quadro.
            self.frame += 1
 
            # Verifica se já chegou no final da animação.
            if self.frame == len(self.explosion_anim):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
 

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
 
        self.image = img
        self.rect = self.image.get_rect()
        #Posição do Shield
        self.rect.x = random.randint(250, WIDTH-ball_width)
        self.rect.y = random.randint(-50, -ball_height)
        #Velocidade do shield
        self.speed_footbal_speedx = random.randint(-2, 2)
        self.speed_football_speedy = random.randint(4, 6)
   
    def update(self):
        global p_up
        if p_up:
            self.rect.x += self.speed_footbal_speedx
            self.rect.y += self.speed_football_speedy
        if self.rect.right > WIDTH or self.rect.top > HEIGHT:
            self.rect.x = random.randint(250, WIDTH-ball_width)
            self.rect.y = random.randint(-50, -ball_height)
            self.speed_football_speedx = random.randint(-2, 2)
            self.speed_football_speedy = random.randint(4, 6)
            p_up = False




#Definindo os frames por segundo para ajustar a velocidade da bola
clock = pygame.time.Clock()
FPS = 30
 
#Criando um grupo bolas
all_balls = pygame.sprite.Group()
all_soccer_balls = pygame.sprite.Group()
 
#Criando o jogador
player = Gk(assets["goalkeeper_img"])
all_balls.add(player)
 
#Criando as bolas
for i in range(5):
    balls = Football(assets["football_img"])
    all_balls.add(balls)
    all_soccer_balls.add(balls)
 

#Definindo o powerup
powerup = PowerUp(assets['powerup'])

 

game = True
t = pygame.time.get_ticks()
p_up = False
while game:
    time_now = pygame.time.get_ticks()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 10
            if event.key == pygame.K_RIGHT:
                player.speedx += 10
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 10
            if event.key == pygame.K_RIGHT:
                player.speedx -= 10
    #Definindo o intervalo de tempo para o powerup aparecer
    if time_now-t >= 10000 and p_up == False:
        p_up = True
        print('entrou')
        t = time_now
    
            

   
    #-----------------------------------
    #---- Atualiza o estado do jogo ----
    #-----------------------------------
 
    #Controlando movimentos das 5 bolas no loop
    all_balls.update()

    powerup.update()


 
    # Verifica se houve colisão entre o goleiro e a bola
    hits = pygame.sprite.spritecollide(player, all_soccer_balls, True)
    for colides in hits:
        x = Football(assets['football_img'])
        all_balls.add(x)
        all_soccer_balls.add(x)
    
    
        

   
    #Adicionando imagens para tela principal
    window.fill((255, 255, 255))
    window.blit(assets["background"], (0, 0))
    # window.blit(assets['powerup'], powerup.rect)
    all_balls.draw(window)
    
    #fazendo o powerup aparecer
    if p_up:
        print('apareceu')
        window.blit(assets['powerup'], powerup.rect)
        # time_p_up = pygame.time.get_ticks()
        # if time_p_up-t >= 5000:
        #     p_up = False
    
    pygame.display.update()



pygame.quit()
 
 