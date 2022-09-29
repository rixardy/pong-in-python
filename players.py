import pygame
from settings import *

class Players: # criando os players

    COLOR = WHITE # definindo a cor dos players
    VEL = 4 # velocidade do player

    def __init__(self, x, y, width, height): # metodo construtor dos players
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win): # definindo onde será desenhado, a cor, posição e tamanho
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height)) 

    def move(self, up=True): # metodo de sentido de movimentação
        if up:
            self.y -= self.VEL # faz subir
        else:
            self.y += self.VEL # faz descer