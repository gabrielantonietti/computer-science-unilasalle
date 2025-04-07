import pygame
import sys


pygame.init()


largura, altura = 300, 200
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Sprite Animation with Button")


branco = (255, 255, 255)
cinza = (200, 200, 200)
preto = (0, 0, 0)


try:
    sprite_sheet = pygame.image.load("Attack.png").convert_alpha()
except:
    
    sprite_sheet = pygame.Surface((1024, 128), pygame.SRCALPHA)
    pygame.draw.rect(sprite_sheet, (255, 0, 0), (0, 0, 1024, 128))


num_quadros = 8
total_width = sprite_sheet.get_width()
total_height = sprite_sheet.get_height()


left_margin = 30    
right_margin = 10   
top_margin = 52     
bottom_margin = 0   


quadro_largura = (total_width // num_quadros) - left_margin - right_margin
quadro_altura = total_height - top_margin - bottom_margin


quadros = []
for i in range(num_quadros):
    x = (i * (total_width // num_quadros)) + left_margin
    y = top_margin
    quadros.append(sprite_sheet.subsurface((x, y, quadro_largura, quadro_altura)))


def desenha_botao(tela, cor, pos, tamanho, texto):
    fonte = pygame.font.Font(None, 36)
    pygame.draw.rect(tela, cor, (pos[0], pos[1], tamanho[0], tamanho[1]))
    texto_surface = fonte.render(texto, True, preto)
    texto_rect = texto_surface.get_rect(center=(pos[0] + tamanho[0]//2, pos[1] + tamanho[1]//2))
    tela.blit(texto_surface, texto_rect)


largura_botao, altura_botao = 100, 50
x_botao = largura - largura_botao - 10
y_botao = altura - altura_botao - 10
botao_rect = pygame.Rect(x_botao, y_botao, largura_botao, altura_botao)


indice_quadro = 0
tempo_animacao = 200
ultimo_tempo = pygame.time.get_ticks()


pos_x = 10
pos_y = 10
velocidade = 2


clock = pygame.time.Clock()
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if botao_rect.collidepoint(evento.pos):
                rodando = False

    
    teclas = pygame.key.get_pressed()
    movimento_x = (teclas[pygame.K_RIGHT] - teclas[pygame.K_LEFT]) * velocidade
    movimento_y = (teclas[pygame.K_DOWN] - teclas[pygame.K_UP]) * velocidade

    
    nova_pos_x = pos_x + movimento_x
    nova_pos_y = pos_y + movimento_y

    
    pos_x = max(0, min(largura - quadro_largura, nova_pos_x))
    pos_y = max(0, min(altura - quadro_altura, nova_pos_y))

    
    sprite_rect = pygame.Rect(pos_x, pos_y, quadro_largura, quadro_altura)
    if sprite_rect.colliderect(botao_rect):
        if movimento_x > 0:
            pos_x = botao_rect.left - quadro_largura
        elif movimento_x < 0:
            pos_x = botao_rect.right
        if movimento_y > 0:
            pos_y = botao_rect.top - quadro_altura
        elif movimento_y < 0:
            pos_y = botao_rect.bottom

    
    agora = pygame.time.get_ticks()
    if agora - ultimo_tempo > tempo_animacao:
        indice_quadro = (indice_quadro + 1) % num_quadros
        ultimo_tempo = agora

    
    tela.fill(branco)
    tela.blit(quadros[indice_quadro], (pos_x, pos_y))
    desenha_botao(tela, cinza, (x_botao, y_botao), (largura_botao, altura_botao), "Sair")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()