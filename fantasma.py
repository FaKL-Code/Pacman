import pygame

from jogo import Jogo

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

class Fantasma(Jogo):
    def __init__(self, cor, tamanho, screen) -> None:
        self.coluna = 6
        self.linha = 8
        self.cor = cor
        self.tamanho = tamanho
        self.draw(screen)
    
    def draw(self, screen):
        fatia = self.tamanho // 9
        px = int(self.coluna * self.tamanho)
        py = int(self.linha * self.tamanho)
        contorno = [(px, py + self.tamanho), (px + fatia, py + fatia * 2),
                    (px + fatia * 2, py + fatia), (px + fatia * 3, py),
                    (px + fatia * 5, py), (px + fatia * 6, py + fatia),
                    (px + fatia * 7, py + fatia * 2), (px + self.tamanho,py + self.tamanho),
                    (px + self.tamanho, py + fatia * 8), (px + fatia * 8, py + self.tamanho),
                    (px + fatia * 2, py + self.tamanho), (px + fatia * 2, py + fatia * 8),
                    (px + fatia, py + self.tamanho), (px, py + fatia * 8), (px, py + self.tamanho)]
        pygame.draw.polygon(screen, self.cor, contorno, 0)
        
        olho_raio_ext = fatia
        olho_raio_int = fatia // 2
        
        olho_e_x = px + fatia * 3
        olho_e_y = py + fatia * 3
        
        olho_d_x = px + fatia * 6
        olho_d_y = py + fatia * 3
        
        pygame.draw.circle(screen, BRANCO, (olho_e_x, olho_e_y), olho_raio_ext, 0)
        pygame.draw.circle(screen, PRETO, (olho_e_x, olho_e_y), olho_raio_int, 0)   
        
        pygame.draw.circle(screen, BRANCO, (olho_d_x, olho_d_y), olho_raio_ext, 0)
        pygame.draw.circle(screen, PRETO, (olho_d_x, olho_d_y), olho_raio_int, 0)    
    
    def calcular_regras(self):
        pass
    
    def processar_eventos(self, evts):
        pass