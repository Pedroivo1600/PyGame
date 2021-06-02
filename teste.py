
import pygame
import random
#Inicia o jogo
pygame.init()
WIDTH = 500 # largura da tela
HEIGHT = 400 # altura da tela
#Fazendo o background aparecer
window = pygame.display.set_mode((WIDTH, HEIGHT))
imagem_tela=pygame.image.load('img/Pitch 1.png').convert_alpha()
imagem_tela=pygame.transform.scale(imagem_tela, (WIDTH, HEIGHT))
window.fill((0, 0, 0))  # Preenche com a cor branca
window.blit(imagem_tela, (0, 0))
game=True
pygame.display.update()
pygame.quit()