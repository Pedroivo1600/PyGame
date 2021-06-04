
import pygame
import random
from config import WIDTH, HEIGHT


#Inicia o jogo
pygame.init()
pygame.mixer.init()
from gamescreen import gamescreen
pygame.mixer.music.set_volume(0.4)

#Criando a tela do jogo
window = pygame.display.set_mode((WIDTH, HEIGHT)) 
gamescreen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados