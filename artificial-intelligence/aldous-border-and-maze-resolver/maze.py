import pygame
import sys
import copy
import random
import time
from random import randint

from resolvedor import resolver_labirinto
from resolvedor_bfs import resolver_labirinto_bfs

class ArestasFechadas:
    def __init__(self, superior, inferior, esquerda, direita):
        self.superior = superior
        self.inferior = inferior
        self.esquerda = esquerda
        self.direita = direita

class Celula:
    def __init__(self, arestasFechadas, corPreenchimento, corVisitada, corLinha, corAberta, visitada, aberta):
        self.arestasFechadas = arestasFechadas
        self.corPreenchimento = corPreenchimento
        self.corVisitada = corVisitada
        self.corLinha = corLinha
        self.corAberta = corAberta
        self.visited = visitada
        self.aberta = aberta
        self.entrada = False
        self.saida = False
        self.caminho_visitado = False

    def desenhar(self, tela, x, y, aresta):
        arSuperiorIni = (x, y)
        arSuperiorFim = (x + aresta, y)
        arInferiorIni = (x, y + aresta)
        arInferiorFim = (x + aresta, y + aresta)
        arEsquerdaIni = (x, y)
        arEsquerdaFim = (x, y + aresta)
        arDireitaIni = (x + aresta, y)
        arDireitaFim = (x + aresta, y + aresta)

        pygame.draw.rect(tela, self.corPreenchimento, (x, y, aresta, aresta))

        if self.arestasFechadas.superior:
            pygame.draw.line(tela, self.corLinha, arSuperiorIni, arSuperiorFim)
        if self.arestasFechadas.inferior:
            pygame.draw.line(tela, self.corLinha, arInferiorIni, arInferiorFim)
        if self.arestasFechadas.esquerda:
            pygame.draw.line(tela, self.corLinha, arEsquerdaIni, arEsquerdaFim)
        if self.arestasFechadas.direita:
            pygame.draw.line(tela, self.corLinha, arDireitaIni, arDireitaFim)

class AldousBroder:
    def __init__(self, qtLinhas, qtColunas, aresta, celulaPadrao):
        self.matriz = Malha(qtLinhas, qtColunas, aresta, celulaPadrao)
        self.qtLinhas = qtLinhas
        self.qtColunas = qtColunas
        self.aresta = aresta
        self.celulaPadrao = celulaPadrao

    def resetaLabirinto(self):
        for linha in range(self.qtLinhas):
            for coluna in range(self.qtColunas):
                self.matriz[linha][coluna] = copy.deepcopy(self.celulaPadrao)

    def SorteiaCelulaVizinha(self, linhaCelulaAtual, colunaCelulaAtual):
        direcoes = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(direcoes)
        for dl, dc in direcoes:
            nl = linhaCelulaAtual + dl
            nc = colunaCelulaAtual + dc
            if 0 <= nl < self.qtLinhas and 0 <= nc < self.qtColunas:
                return nl, nc
        return linhaCelulaAtual, colunaCelulaAtual

    def GeraLabirinto(self):
        self.resetaLabirinto()
        unvisitedCells = self.qtLinhas * self.qtColunas
        currentCellLine = randint(0, self.qtLinhas - 1)
        currentCellColumn = randint(0, self.qtColunas - 1)
        self.matriz[currentCellLine][currentCellColumn].visited = True
        unvisitedCells -= 1

        while unvisitedCells > 0:
            neighCellLine, neighCellColumn = self.SorteiaCelulaVizinha(currentCellLine, currentCellColumn)

            if not self.matriz[neighCellLine][neighCellColumn].visited:
                curr = self.matriz[currentCellLine][currentCellColumn].arestasFechadas
                neigh = self.matriz[neighCellLine][neighCellColumn].arestasFechadas

                deltaLinha = neighCellLine - currentCellLine
                deltaColuna = neighCellColumn - currentCellColumn

                if deltaLinha == -1 and deltaColuna == 0:
                    curr.superior = False
                    neigh.inferior = False
                elif deltaLinha == 1 and deltaColuna == 0:
                    curr.inferior = False
                    neigh.superior = False
                elif deltaLinha == 0 and deltaColuna == -1:
                    curr.esquerda = False
                    neigh.direita = False
                elif deltaLinha == 0 and deltaColuna == 1:
                    curr.direita = False
                    neigh.esquerda = False
                else:
                    continue

                self.matriz[neighCellLine][neighCellColumn].visited = True
                unvisitedCells -= 1

            currentCellLine, currentCellColumn = neighCellLine, neighCellColumn

        linha_entrada, coluna_entrada = 1, 0
        linha_saida, coluna_saida = self.qtLinhas - 1, self.qtColunas - 1

        entrada = self.matriz[linha_entrada][coluna_entrada]
        saida = self.matriz[linha_saida][coluna_saida]

        entrada.arestasFechadas.esquerda = False
        saida.arestasFechadas.inferior = False

        entrada.corPreenchimento = (255, 0, 0)
        saida.corPreenchimento = (0, 255, 0)
        entrada.entrada = True
        saida.saida = True

class Malha:
    def __init__(self, qtLinhas, qtColunas, aresta, celulaPadrao):
        self.qtLinhas = qtLinhas
        self.qtColunas = qtColunas
        self.aresta = aresta
        self.celulaPadrao = celulaPadrao
        self.matriz = self.GeraMatriz()

    def __getitem__(self, index):
        return self.matriz[index]

    def __setitem__(self, index, value):
        self.matriz[index] = value

    def GeraMatriz(self):
        return [[copy.deepcopy(self.celulaPadrao) for _ in range(self.qtColunas)] for _ in range(self.qtLinhas)]

    def DesenhaLabirinto(self, tela, x, y):
        for linha in range(self.qtLinhas):
            for coluna in range(self.qtColunas):
                self.matriz[linha][coluna].desenhar(tela, x + coluna * self.aresta, y + linha * self.aresta, self.aresta)

def main():
    pygame.init()

    largura, altura = 600, 600
    N = 41
    M = 41
    aresta = 10

    preto = (0, 0, 0)
    visitada = (128, 128, 128)
    branco = (255, 255, 255)
    rosa = (255, 192, 203)
    azul = (0, 0, 255)
    laranja = (255, 165, 0)
    
    celulaPadrao = Celula(
        ArestasFechadas(True, True, True, True),
        preto,          # corPreenchimento inicial (preto)
        visitada,    # corVisitada
        branco,    # corLinha
        branco,    # corAberta
        False, False        # visitada, aberta
    )

    labirinto = AldousBroder(N, M, aresta, celulaPadrao)
    labirinto.GeraLabirinto()

    # Resolvendo com força bruta (DFS)
    inicio_fb = time.time()
    caminho_forca_bruta = resolver_labirinto(labirinto.matriz.matriz)
    fim_fb = time.time()

    # Resolvendo com BFS
    inicio_bfs = time.time()
    caminho_bfs = resolver_labirinto_bfs(labirinto.matriz.matriz)
    fim_bfs = time.time()

    set_dfs = set(caminho_forca_bruta) if caminho_forca_bruta else set()
    set_bfs = set(caminho_bfs) if caminho_bfs else set()

    for pos in set_dfs.union(set_bfs):
        linha, coluna = pos
        celula = labirinto.matriz[linha][coluna]
        if pos in set_dfs and pos in set_bfs:
            celula.corPreenchimento = rosa
        elif pos in set_dfs:
            celula.corPreenchimento = azul
        elif pos in set_bfs:
            celula.corPreenchimento = laranja

    print(f"Tempo força bruta (DFS): {fim_fb - inicio_fb:.4f} segundos")
    print(f"Tempo BFS: {fim_bfs - inicio_bfs:.4f} segundos")

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Mostra Malha')

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tela.fill(branco)  
        offset_x = (largura - M * aresta) // 2
        offset_y = (altura - N * aresta) // 2
        labirinto.matriz.DesenhaLabirinto(tela, offset_x, offset_y)
        pygame.display.flip()

if __name__ == '__main__':
    main()
