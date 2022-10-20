import pygame

AMARELO = (255, 255, 0)
VELOCIDADE = 0.1


pygame.init()

tela = pygame.display.set_mode((640, 480))

xpos = 30
ypos = 240

vel_x = VELOCIDADE
vel_y = VELOCIDADE

raio = 30

while True:
    
    xpos += vel_x
    
    ypos += vel_y
    
    if xpos > 640 - raio:
        vel_x = -VELOCIDADE
    elif xpos < 0 + raio:
        vel_x = VELOCIDADE
        
    if ypos > 480 - raio:
        vel_y = -VELOCIDADE
    elif ypos < 0 + raio:
        vel_y = VELOCIDADE
    
    tela.fill((0, 0, 0))
    pygame.draw.circle(tela, AMARELO, (int(xpos), ypos), raio, 0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
