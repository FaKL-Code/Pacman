import pygame

from pacman import Pacman
from cenario import Cenario
from fantasma import Fantasma

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
CIANO = (0, 255, 255)
LARANJA = (255, 127, 0)
ROSA = (255, 0, 255)

screen = pygame.display.set_mode((800, 600), 0)
size = 600//30
pacman = Pacman(size)
blinky = Fantasma(VERMELHO, size, screen)
inky = Fantasma(CIANO, size, screen)
clyde = Fantasma(LARANJA, size, screen)
pinky = Fantasma(ROSA, size, screen)

cenario = Cenario(size, pacman)
cenario.adicionar_movel(pacman)
cenario.adicionar_movel(blinky)
cenario.adicionar_movel(inky)
cenario.adicionar_movel(clyde)
cenario.adicionar_movel(pinky)


if __name__ == '__main__':
    while True:
        pacman.calcular_regras()
        cenario.calcular_regras()
        blinky.calcular_regras()
        inky.calcular_regras()
        clyde.calcular_regras()
        pinky.calcular_regras()

        screen.fill(PRETO)
        cenario.draw(screen)
        pacman.draw(screen)
        blinky.draw(screen)
        inky.draw(screen)
        clyde.draw(screen)
        pinky.draw(screen)
                
        pygame.display.update()
        pygame.time.delay(100)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pacman.processar_eventos(events)
        cenario.processar_eventos(events)
        pygame.display.update() 
                    