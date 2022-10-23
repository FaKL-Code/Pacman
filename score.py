import pygame

pygame.font.init()
    
AMARELO = (255, 255, 0)

font = pygame.font.SysFont("arial", 20, True, False)

class Score():
    def draw_score(tamanho, screen, pontos, vidas):
        pontos_x = 29 * tamanho
        pontos_img = font.render(f"Score {pontos}", True, AMARELO)
        screen.blit(pontos_img, (pontos_x, 50))
        vidas_img = font.render(f"Vidas {vidas}", True, AMARELO)
        screen.blit(vidas_img, (pontos_x, 80))