import pygame
import random
#Inicia o jogo
pygame.init()
pygame.mixer.init()


#----------------
# --Variáveis----      
#----------------

list_lives = [] #lista de vidas
shield = False #boolean que indica se o powerup "Shield" está aparecendo no jogo ou não
p_up = False #boolean que indica se o jogador colidiu com o  powerup no jogo ou não
FPS = 30
#MEDIDAS
#Medidas do background (estadio)
WIDTH = 500 # largura da tela
HEIGHT = 400 # altura da tela
tela_inicio = window = pygame.display.set_mode((WIDTH, HEIGHT)) #cria a tela do jogo
window = pygame.display.set_mode((WIDTH, HEIGHT)) #cria a tela do jogo

# Printando na tela
font = pygame.font.SysFont(None, 48)
font1= pygame.font.SysFont(None, 80)
Titulo = font1.render('Goalkepper Pro', True, (140, 50, 50))
start = font.render('Press "enter" to start', True, (0, 0, 0))
game_over = font1.render('Game Over', True, (0, 0, 0))
novamente = font.render('Quer jogar novamente? Pressione Enter', True, (0, 0, 0))

#Medidas das bolas
ball_width = 30 #largura da bola
ball_height = 20 # altura da bola
 
#Medidas do goleiro
gk_width = 70 # largura do goleiro
gk_height = 60 # altura do goleiro


#Carregando sons do jogo
pygame.mixer.music.set_volume(0.4)
goal_sound = pygame.mixer.Sound('sounds/grito_de_gol.mp3')
save_sound = pygame.mixer.Sound('sounds/quase_gol.mp3')

 
#Inicia assets

def load_assets():
    assets = {}
    assets['background'] =  pygame.image.load('img/estadio.png').convert() #guarda a imagem do background que aparecerá no jogo
    assets["background"] = pygame.transform.scale(assets["background"], (WIDTH, HEIGHT)) # define a altura e largura do background
    assets['football_img'] =  pygame.image.load('img/football.png').convert_alpha() #guarda a imagem da bola de futebol
    assets['football_img'] = pygame.transform.scale(assets["football_img"], (ball_width, ball_height)) #define a altura e lagura da bola de futebol no jogo
    assets['goalkeeper_img'] = pygame.image.load('img/Goalkeeper.png').convert_alpha()#guarda a imagem do goleiro que aparecerá no jogo
    assets['goalkeeper_img'] = pygame.transform.scale(assets["goalkeeper_img"], (gk_width, gk_height))#define a altura e lagura do goleiro no jogo
    assets['powerup'] = pygame.image.load('img/powerup_shield.png').convert_alpha() #guarda a imagem do powerup "Shield" que aparecerá no jogo  
    assets['powerup'] = pygame.transform.scale(assets['powerup'], (ball_width, ball_height)) #define a altura e lagura do powerup "Shield" no jogo
    assets["score_font"] = pygame.font.Font('font/SoccerLeague.ttf', 28) #guarda a fonte da pontuação que aparecerá no jogo
    assets["score_font_2"] = pygame.font.Font('font/PressStart2P.ttf', 28)#guarda a fonte da vida do jogador que aparecerá no jogo
    assets['golden_keeper'] = pygame.image.load('img/Golden_keeper.png').convert_alpha()
    assets['golden_keeper'] = pygame.transform.scale(assets['golden_keeper'], (gk_width, gk_height))
    assets['tela de inicio'] =  pygame.image.load('img/Pitch 1.png').convert() 
    assets["tela de inicio"] = pygame.transform.scale(assets["tela de inicio"], (WIDTH, HEIGHT))
    assets['final'] =  pygame.image.load('img/final.jfif').convert() 
    assets["final"] = pygame.transform.scale(assets["final"], (WIDTH, HEIGHT))
    return assets

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
 
    def update(self):
        global shield
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
    def update(self):
        global shield # Chama a variável "shield" definida previamente (definida incialmente como "shield = False")

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
    def update(self):
        
        # Chama a variável "p_up" definida previamente (definida incialmente como "p_up = False")
        global p_up 
        
        #Posição do power up quando ele está aparencendo no jogo
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
    
    #Se o jogador colidir com o power up, o código abaixo faz com que o power up continue aparecendo
    def update_collide(self):
        if not p_up:
            self.rect.x = random.randint(250, WIDTH-100)
            self.rect.y = random.randint(-50, -ball_height)
            self.speed_football_speedx = random.randint(-2, 2)
            self.speed_football_speedy = random.randint(4, 6)



#============================
#-------Loop Principal-------
#============================

def gamescreen(window):
    global shield , p_up
    
    assets = load_assets()

    tempo_p_up = 20000
    
    #Definindo os frames por segundo para ajustar a velocidade da bola
    clock = pygame.time.Clock()
 
    #Criando grupos
    all_balls = pygame.sprite.Group()
    all_power_ups = pygame.sprite.Group()
    all_soccer_balls = pygame.sprite.Group()
    groups = {}
    groups["all_balls"] = all_balls
    groups["all_soccer_balls"] = all_soccer_balls
    groups["all_power_ups"] = all_power_ups
 
    #Criando o jogador
    player = Gk(assets["goalkeeper_img"], assets['golden_keeper'])
    all_balls.add(player)

    
    #Criando as bolas
    for i in range(5):
        balls = Football(assets["football_img"])
        all_balls.add(balls)
        all_soccer_balls.add(balls)

    #Criando o powerup
    powerup = PowerUp(assets['powerup'])
    all_power_ups.add(powerup)

    #Estado do jogo
    DONE = 0 #o jogo terminou
    PLAYING = 1 #o jogador está jogando
    TELA = 2
    FINAL = 3
    state = TELA #definindo o estado inicial do jogo como PLAYING

    #Inicia o placar com 0 pontos
    pontos = 0

    #Cria um dicionário de teclas que guarda se alguma tecla estava pressionada ou não
    keys_down = {}

    #Inicia o número total de vidas como 3
    vidas = 3

    t = pygame.time.get_ticks()
    #Trata eventos
    while state == TELA:
        window.fill((255, 255, 255))
        window.blit(assets["tela de inicio"], (0, 0))
        window.blit(Titulo,(50,150))
        window.blit(start,(90,250))
        pygame.display.update() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            if state == TELA:
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_RETURN:
                            state = PLAYING
           
                        
    while state == PLAYING: 
        time_now = pygame.time.get_ticks()
        clock.tick(FPS)
        for event in pygame.event.get():
            #Verifica consequencias
            if event.type == pygame.QUIT:
                state = DONE
            if state == PLAYING:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 15
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 15
             # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 15
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 15
        #Definindo o intervalo de tempo para o powerup aparecer
        if time_now-t >= tempo_p_up and p_up == False:
            p_up = True
            t = time_now
    
        #-----------------------------------
        #---- Atualiza o estado do jogo ----
        #-----------------------------------
 
        #Controlando movimentos das 5 bolas no loop
        all_balls.update()
        powerup.update()

        # Verifica se houve colisão entre o goleiro e a bola
        if state == PLAYING:
            #Quando o goleiro pega a bola
            hits = pygame.sprite.spritecollide(player, all_soccer_balls, True)
            for colides in hits:
                pygame.mixer.music.set_volume(0.1)
                save_sound.play()
                x = Football(assets['football_img'])
                all_balls.add(x)
                all_soccer_balls.add(x)
                #Ganha pontos
                pontos += 10
        
            #Quando o goleiro pega o powerup
            hits_p_up = pygame.sprite.spritecollide(player,all_power_ups,False)
            for colides in hits_p_up:
                shield = True
                t_shield = pygame.time.get_ticks()
                p_up = False
                powerup.update_collide()
            if shield:
                if time_now - t_shield >= 10000:
                    shield = False
        
            #Quando o goleiro não defende a bola
            if len(list_lives) == 1:
                vidas = 2
            if len(list_lives) == 2:
                vidas = 1
            if len(list_lives) == 3:
                vidas = 0
            if len(list_lives) == 4:
                state = FINAL #Se o goleiro chegar a 0 vidas o jogo termina


    #=====================================================
    #-------Adicionando imagens para tela principal-------
    #=====================================================

        #Fazendo o background aparecer
        window.fill((255, 255, 255))
        window.blit(assets["background"], (0, 0))
        all_balls.draw(window)
    
        #Fazendo o powerup aparecer
        if p_up:
            window.blit(assets['powerup'], powerup.rect)

        # Desenhando o placar
        text_surface = assets['score_font'].render("{:08d}".format(pontos), True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 6,  HEIGHT- 379)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = assets['score_font_2'].render(chr(9829) * vidas, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (400, HEIGHT - 350)
        window.blit(text_surface, text_rect)

        # Mostra o novo frame para o jogador
        pygame.display.update() 
    
    while state == FINAL:
        window.fill((255, 255, 255))
        window.blit(assets["final"], (0, 0))
        window.blit(game_over,(75,150))
        pygame.display.update() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            if state == FINAL:
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_RETURN:
                        state = PLAYING
                    else:
                        state = DONE

#Fim do loop principal

gamescreen(window)
#=========================
#-------Finalização-------
#=========================

pygame.quit() # Função do PyGame que finaliza os recursos utilizados