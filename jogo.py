import pygame

from abc import abstractmethod, ABCMeta

screen = pygame.display.set_mode((800, 600), 0)

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