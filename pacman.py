import pygame

from jogo import Jogo
from cenario import Cenario

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VELOCIDADE = 0.5

class Pacman:
    def __init__(self, size):
        self.centro_x = 400
        self.centro_y = 300
        self.vel_x = 0
        self.vel_y = 0
        self.tamanho = size
        self.raio = self.tamanho // 2
        self.coluna = 1
        self.linha = 1
        self.coluna_intent = int(self.coluna)
        self.linha_intent = int(self.linha)
        
    def update(self):
        self.centro_x += self.vel_x
        self.centro_y += self.vel_y

    def calcular_regras(self):
        self.coluna_intent = self.coluna + self.vel_x
        self.linha_intent = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)
            
    def draw(self, screen):
        pygame.draw.circle(screen, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)
        
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        
        pygame.draw.polygon(screen, PRETO, pontos, 0)
        
        olho_x = self.centro_x + self.raio / 3
        olho_y = self.centro_y - self.raio * 0.7
        olho_raio = self.raio / 5
        pygame.draw.circle(screen, PRETO, (olho_x, olho_y), olho_raio, 0)   

    def processa_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = VELOCIDADE
                elif e.key == pygame.K_LEFT:
                    self.vel_x = -VELOCIDADE
                elif e.key == pygame.K_UP:
                    self.vel_y = -VELOCIDADE
                elif e.key == pygame.K_DOWN:
                    self.vel_y = VELOCIDADE
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = 0
                elif e.key == pygame.K_LEFT:
                    self.vel_x = 0
                elif e.key == pygame.K_UP:
                    self.vel_y = 0
                elif e.key == pygame.K_DOWN:
                    self.vel_y = 0
                                    
    def aceitar_movimento(self):
        self.linha = self.linha_intent
        self.coluna = self.coluna_intent