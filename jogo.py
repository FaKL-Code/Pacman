import pygame

from abc import abstractmethod, ABCMeta

screen = pygame.display.set_mode((800, 600), 0)

fonte = pygame.font.SysFont('arial', 24, True, False)

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VELOCIDADE = 0.01

class Jogo(metaclass=ABCMeta):
    @abstractmethod
    def draw(self, screen):
        pass
    
    @abstractmethod
    def calcular_regras(self):
        pass
    
    @abstractmethod
    def processar_eventos(self, events):
        pass