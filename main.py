import pygame

from pacman import Pacman
from cenario import Cenario
from fantasma import Fantasma

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

screen = pygame.display.set_mode((800, 600), 0)
size = 600//30
pacman = Pacman(size)
blinky = Fantasma(VERMELHO, size, screen)
cenario = Cenario(size, pacman, blinky)

if __name__ == '__main__':
    while True:
        pacman.calcular_regras()
        cenario.calcular_regras()
        blinky.calcular_regras()

        screen.fill(PRETO)
        cenario.draw(screen)
        pacman.draw(screen)
        blinky.draw(screen)
        pygame.display.update()
        pygame.time.delay(100)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pacman.processa_eventos(events)
        cenario.processar_eventos(events)
        pygame.display.update() 
                    