# definindo os parametros da janela
import pygame

TITLE = "Pong"
WIDTH = 1280 # largura
HEIGHT = 720 # altura
FPS = 60 # taxa de atualização
WHITE = (255, 255, 255) # cor branca em RGB
BLACK = (0, 0, 0) # cor preta em RGB
PLAYER_WIDHT = 30
PLAYER_HEIGHT = 140
RAIO_BOLA = 10
VEL_OPONENTE = 10
RELOGIO = pygame.time.Clock() #3 criando instancia do relogio
CARREGAMENTO = 100000000 # tempo de carregamento da barra
emJogo = True # variavel de controle pra saber se o jogo está rodando