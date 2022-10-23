import pygame

pygame.font.init()
    
AMARELO = (255, 255, 0)

font = pygame.font.SysFont("arial", 20, True, False)

class Score():
    def draw_score(tamanho, screen, pontos):
        pontos_x = 29 * tamanho
        pontos_img = font.render("Score {}".format(pontos), True, AMARELO)
        screen.blit(pontos_img, (pontos_x, 50))