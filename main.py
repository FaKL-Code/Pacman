import pygame

from pacman import Pacman
from cenario import Cenario
from fantasma import Fantasma


size = 600//30
pacman = Pacman(size)
cenario = Cenario(size, pacman)

while True:
    pacman.calcular_regras()
    cenario.calcular_regras()
    
    screen.fill(PRETO)
    cenario.draw(screen)
    pacman.draw(screen)
    pygame.display.update()
    pygame.time.delay(100)
            
    events = pygame.event.get()
    pacman.processa_eventos(events)
    cenario.processar_eventos(events)
                 