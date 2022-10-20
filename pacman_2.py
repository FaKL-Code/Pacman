import pygame

pygame.init

screen = pygame.display.set_mode((800, 600), 0)

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)

class Pacman:
    def __init__(self):
        self.centro_x = 400
        self.centro_y = 300
        self.x = 30
        self.y = 240
        self.vel_x = 0.1
        self.vel_y = 0.1
        self.tamanho = 100
        self.raio = self.tamanho // 2
        self.cor = AMARELO
        
    def update(self):
        self.centro_x += self.vel_x
        self.centro_y += self.vel_y
        
        if self.centro_x > 800 - self.raio:
            self.vel_x = -0.1
        elif self.centro_x < 0 + self.raio:
            self.vel_x = 0.1
            
        if self.centro_y > 600 - self.raio:
            self.vel_y = -0.1
        elif self.centro_y < 0 + self.raio:
            self.vel_y = 0.1
            
    def draw(self, screen):
        pygame.draw.circle(screen, self.cor, (self.centro_x, self.centro_y), self.raio, 0)
        
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        
        pygame.draw.polygon(screen, PRETO, pontos, 0)
        
        olho_x = self.centro_x + self.raio / 3
        olho_y = self.centro_y - self.raio * 0.7
        olho_raio = self.raio / 5
        pygame.draw.circle(screen, PRETO, (olho_x, olho_y), olho_raio, 0)
        
if __name__ == '__main__':
    pacman = Pacman()
    
    while True:
        pacman.update()
        
        screen.fill((0, 0, 0))
        pacman.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        pygame.display.update()
