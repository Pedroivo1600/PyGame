import pygame
import os
from config import WIDTH, HEIGHT, gk_width, gk_height,ball_width, ball_height

#==============================
#--Carregando os sons do jogo--
#==============================

#----Som
goal_sound = pygame.mixer.Sound('sounds/grito_de_gol.mp3') 
save_sound = pygame.mixer.Sound('sounds/quase_gol.mp3')

#==========================================================================
#--Carregando e definindo as dimensões das fontes da tela inicial e final--
#==========================================================================


#----Tamanho da fonte que aparece na tela inicial e final
font = pygame.font.SysFont(None, 48)
font1= pygame.font.SysFont(None, 80)

#***Mostrando as fontes na tela****
Titulo = font1.render('Goalkepper Pro', True, (140, 50, 50))
start = font.render('Press "enter" to start', True, (0, 0, 0))
game_over = font1.render('Game Over', True, (0, 0, 0))
novamente = font.render('Quer jogar novamente? Pressione Enter', True, (0, 0, 0))


#======================================
#--Definição das imagens e das fontes--
#======================================

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
    assets['golden_keeper'] = pygame.image.load('img/Golden_keeper.png').convert_alpha()#guarda a imagem do goleiro quando ele pega o power up
    assets['golden_keeper'] = pygame.transform.scale(assets['golden_keeper'], (gk_width, gk_height))#redimensiona a imagem salva na variavel acima para ficar no tamanho do goleiro
    assets['tela de inicio'] =  pygame.image.load('img/Pitch 1.png').convert() 
    assets["tela de inicio"] = pygame.transform.scale(assets["tela de inicio"], (WIDTH, HEIGHT))
    assets['final'] =  pygame.image.load('img/final.jfif').convert() 
    assets["final"] = pygame.transform.scale(assets["final"], (WIDTH, HEIGHT))
    return assets