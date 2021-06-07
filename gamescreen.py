import pygame
import random
from config import FPS, WIDTH, HEIGHT, list_lives, shield
from assets import load_assets, start, save_sound, Titulo, game_over
from sprites import Gk, Football, PowerUp

#============================
#-------Loop Principal-------
#============================

def gamescreen(window):
    global shield
    p_up = False #boolean que indica powerup aparece no jogo ou não

    assets = load_assets()

    
    
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
    pygame.mixer.music.play(loops=-1)
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
           
    pygame.mixer.music.play(loops=-1)                 
    while state == PLAYING: 
        tempo_p_up = random.randint(25000, 40000)
        print(tempo_p_up)
        # main_sound.play()
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
        all_balls.update(shield)
        powerup.update(p_up)
        powerup.update_collide(p_up)


        # Verifica se houve colisão entre o goleiro e a bola
        if state == PLAYING:
            #Quando o goleiro pega a bola
            hits = pygame.sprite.spritecollide(player, all_soccer_balls, True)
            for colides in hits:
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
                p_up = powerup.update_collide(p_up)
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
            print("p_up do blit {0}".format(p_up))
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
