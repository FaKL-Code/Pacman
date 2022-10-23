import random
from tkinter import font
import pygame
from fantasma import Fantasma

from jogo import Jogo
from score import Score

pygame.font.init()

font = pygame.font.SysFont("arial", 20, True, False)

screen = pygame.display.set_mode((800, 600), 0)

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)

ACIMA = 1
ABAIXO = 2
DIREITA = 3
ESQUERDA = 4

JOGANDO = 0
PAUSE = 1
GAMEOVER = 2
WIN = 3

class Cenario(Jogo):
    def __init__(self, tamanho, pacman):
        self.pacman = pacman
        self.moveis = []
        self.tamanho = tamanho
        self.pontos = 0
        self.estado = JOGANDO
        self.matriz = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 3, 3, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 3, 3, 3, 3, 3, 3, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 3, 3, 3, 3, 3, 3, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 3, 3, 3, 3, 3, 3, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]

    def adicionar_movel(self, obj):
        self.moveis.append(obj)
    
    def draw_line(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            half = self.tamanho // 2
            cor = PRETO
            if coluna == 2:
                cor = AZUL
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
            if coluna == 1:
                pygame.draw.circle(tela, AMARELO, (x + half, y + half),self.tamanho // 10, 0)
                
    def draw(self, tela):
        if self.estado == JOGANDO:
            self.draw_jogando(tela)
        elif self.estado == PAUSE:
            self.draw_jogando(tela)
            self.draw_center_text(tela, "P A U S E")
        elif self.estado == GAMEOVER:
            self.draw_jogando(tela)
            self.draw_center_text(tela, "G A M E  O V E R")
        elif self.estado == WIN:
            self.draw_jogando(tela)
            self.draw_center_text(tela, "Y O U  W I N")
    
    def draw_center_text(self, tela, text):
        img_text = font.render(text, True, AMARELO)
        tx = (tela.get_width() - img_text.get_width()) // 2
        ty = (tela.get_height() - img_text.get_height()) // 2
        tela.blit(img_text, (tx, ty))        

    def draw_jogando(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.draw_line(tela, numero_linha, linha)
        Score.draw_score(self.tamanho, tela, self.pontos)

    def calcular_regras(self):
        if self.estado == JOGANDO:
            self.calcular_regras_jogando()
        elif self.estado == PAUSE:
            self.calcular_regras_pause()
        elif self.estado == GAMEOVER:
            self.calcular_regras_gameover()
        elif self.estado == WIN:
            self.calcular_regras_win()
            
    def calcular_regras_win(self):
        pass
            
    def calcular_regras_gameover(self):
        pass
            
    def calcular_regras_pause(self):
        pass

    def calcular_regras_jogando(self):
        for mov in self.moveis:
            lin = int(mov.linha)
            col = int(mov.coluna)
            lin_intencao = int(mov.linha_intent)
            col_intencao = int(mov.coluna_intent)
            direcoes = self.get_direcoes(lin, col)
            
            if len(direcoes) >= 3:
                if self.matriz[lin][col] == 3:
                    direcao_inicial = [ACIMA]
                    mov.esquina(direcao_inicial)
                else:
                    mov.esquina(direcoes)
                        
            if isinstance(mov, Fantasma) and int(mov.linha) == int(self.pacman.linha) and int(mov.coluna) == int(self.pacman.coluna):
                self.estado = GAMEOVER
            else:
                if 0 <= lin_intencao < len(self.matriz) and 0 <= col_intencao < len(self.matriz[0]):
                    if self.matriz[lin_intencao][col_intencao] != 2:
                        mov.aceitar_movimento()
                        if self.matriz[lin][col] == 1 and mov == self.pacman:
                            self.pontos += 1
                            self.matriz[lin][col] = 0
                            if not any(1 in linha for linha in self.matriz) and not any(1 in coluna for coluna in self.matriz):
                                self.estado = WIN
                    else:
                        mov.recusar_movimento(direcoes)
    
    def processar_eventos(self, evts):
        for e in evts:
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    if self.estado == JOGANDO:
                        self.estado = PAUSE
                    else:
                        self.estado = JOGANDO
                
    def get_direcoes(self, linha, coluna):
        direcoes = []
        if self.matriz[int(linha)][int(coluna - 1)] != 2:
            direcoes.append(ESQUERDA)
        if self.matriz[int(linha)][int(coluna + 1)] != 2:
            direcoes.append(DIREITA)
        if self.matriz[int(linha - 1)][int(coluna)] != 2:
            direcoes.append(ACIMA)
        if self.matriz[int(linha + 1)][int(coluna)] != 2:
            direcoes.append(ABAIXO)
        return direcoes