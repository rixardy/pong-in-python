from tkinter import Button
from turtle import width
import pygame
from settings import *

pygame.init() # GUI do jogo

# desenhando a tela
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # pasando a largura e altura da tela

pygame.display.set_caption(TITLE) # definindo o nome da janela


start_img = pygame.image.load('Start_BTN.png').convert_alpha()
exit_img = pygame.image.load('Exit_BTN.png').convert_alpha()

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    
    def draw(self):

        pos = pygame.mouse.get_pos()
        WIN.blit(self.image, (self.rect.x, self.rect.y))


start_b = Button(300, 280, start_img, 0.5)
exit_b = Button(700, 280, exit_img, 0.5)

run = True
while run:
        
    WIN.fill(WHITE)
    start_b.draw()
    exit_b.draw()

    for event in pygame.event.get(): # rodando todos os eventos e colocando na variavel event
        if event.type == pygame.QUIT: # se o evento acionado for o botão vermelho e fechar
            run = False # informando que parou o loop saiu o jogo
            break
    pygame.display.update()

pygame.quit() # fecha o jogo