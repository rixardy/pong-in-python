from turtle import width
import pygame, threading, sys
from settings import *
from app import *

titulo

FONTE = pygame.font.SysFont("Roboto", 100) #definindo fonte da mensagem de texto

molduraLoad = pygame.image.load("assets/loading_bg.png") # carrega immagem moldura do loading
molduraLoadR = molduraLoad.get_rect(center=(640, 360)) # recupera o retangulo da imagem, define a posicao central e parra pra uma variavel

carregaLoad = pygame.image.load("assets/loading.png") # carrega imagem da barra dee loagding
carregaLoadR = carregaLoad.get_rect(midleft=(280, 360)) # recupera o retangulo da imagem, define a posicao central e parra pra uma variavel

fimLoad = False # variavel de controle do fim do carregamento

def doWork(): # funcao que faz funciona a barra
    global fimLoad, inicioLoad # acesso global as variaveis

    for i in range(CARREGAMENTO):
        math_equation = 523687 / 789456 * 89456
        inicioLoad = i
    
    fimLoad = True # apos o carregamento total o load chega ao fim

threading.Thread(target=doWork).start()

while emJogo: # loop do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()

    WIN.fill("#0d0e2e") # definindo a cor de fundo

    if not fimLoad:
        barraLoad = inicioLoad / CARREGAMENTO * 740

        carregaLoad = pygame.transform.scale(carregaLoad, (int(barraLoad), 100))
        carregaLoadR = carregaLoad.get_rect(midleft=(270, 360))

        WIN.blit(molduraLoad, molduraLoadR) #faz aparecer a moldura daa barra
        WIN.blit(carregaLoad, carregaLoadR) #faz aparecer o carregamento da barra
    else:
        main()

    pygame.display.update() # atualizando a tela
    RELOGIO.tick(60) # definindo FPS