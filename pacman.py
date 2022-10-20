import pygame

AMARELO = (255, 255, 0)


pygame.init()

tela = pygame.display.set_mode((640, 480))

while True:
    
    pygame.draw.circle(tela, AMARELO, (320, 240), 50, 0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    tela.fill((0, 0, 0))

    pygame.display.update()
