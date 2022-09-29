from tkinter import Button
from turtle import right
import pygame # importando o pygame
from settings import * # importando tudo de setting
from players import *
from bola import *

pygame.init() # GUI do jogo

# desenhando a tela
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # pasando a largura e altura da tela

titulo = pygame.display.set_caption(TITLE) # definindo o nome da janela

bola = Bola(WIDTH//2, HEIGHT//2, RAIO_BOLA)

def draw(win, players, bola): # desenhhando a tela e os playes
    WIN.fill(BLACK) # definindo a cor da tela

    for player in players: # pegando todos os players
        player.draw(win) # desenhhando os players na tela

    for i in range(10, HEIGHT, HEIGHT//50):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//200))

    bola.draw(win)
    pygame.display.update() # atualizando a tela

def player_colisao(bola, left_player, right_player):
    if bola.y + bola.radius >= HEIGHT:
        bola.y_vel *= -1
    elif bola.y - bola.radius <= 0:
        bola.y_vel *= -1

    if bola.x_vel < 0:
        if bola.y >= left_player.y and bola.y <= left_player.y + left_player.height:
            if bola.x - bola.radius <= left_player.x + left_player.width:
                bola.x_vel *= -1

                middle_y = left_player.y + left_player.height /2
                differeence_in_y = middle_y - bola.y
                reduction_factor = (left_player.height / 2) / bola.MAX_VEL
                y_vel = differeence_in_y / reduction_factor
                bola.y_vel = -1 * y_vel
    else:
        if bola.y >= right_player.y and bola.y <= right_player.y + right_player.height:
            if bola.x + bola.radius >= right_player.x:
                bola.x_vel *= -1

                middle_y = right_player.y + right_player.height /2
                differeence_in_y = middle_y - bola.y
                reduction_factor = (right_player.height / 2) / bola.MAX_VEL
                y_vel = differeence_in_y / reduction_factor
                bola.y_vel = -1 * y_vel

def movimento_players(keys, left_player, right_player): # movimentando os players
        if keys[pygame.K_w] and left_player.y - left_player.VEL >= 0: # delimmitando as posições
            left_player.move(up=True)
        if keys[pygame.K_s] and left_player.y + left_player.VEL + left_player.height <= HEIGHT:
            left_player.move(up=False)

        """if keys[pygame.K_UP] and right_player.y - right_player.VEL >= 0:
            right_player.move(up=True)
        if keys[pygame.K_DOWN] and right_player.y + right_player.VEL + right_player.height <= HEIGHT:
            right_player.move(up=False)"""
        
        if right_player.y + right_player.height < bola.y:
            right_player.y += VEL_OPONENTE
        if right_player.y - right_player.height > bola.y:
            right_player.y -= VEL_OPONENTE

# loop principal
def main():
    
    emJogo = True # variavel de controle pra saber se o jogo está rodando
    
    
    # criando 2 players
    left_player = Players(10, HEIGHT//2 - PLAYER_HEIGHT//2, PLAYER_WIDHT, PLAYER_HEIGHT)
    right_player = Players(WIDTH - 10 - PLAYER_WIDHT, HEIGHT//2 - PLAYER_HEIGHT//2, PLAYER_WIDHT, PLAYER_HEIGHT)
    #bola = Bola(WIDTH//2, HEIGHT//2, RAIO_BOLA)

    while emJogo:
        
        RELOGIO.tick(FPS) # chama o tick do relogio para taxa de atualização da tela
        draw(WIN, [left_player, right_player], bola) #3 desenha a tela e os players

        for event in pygame.event.get(): # rodando todos os eventos e colocando na variavel event
            if event.type == pygame.QUIT: # se o evento acionado for o botão vermelho e fechar
                emJogo = False # informando que parou o loop saiu o jogo
                break
        botoes = pygame.key.get_pressed() # captura todos os pressionamentos de tecla
        movimento_players(botoes, left_player, right_player) # faz movimentar todos os players

        bola.move()
        player_colisao(bola, left_player, right_player)

    pygame.quit() # fecha o jogo

if __name__ == '__main__': # verifica se está sendo executado
    main()