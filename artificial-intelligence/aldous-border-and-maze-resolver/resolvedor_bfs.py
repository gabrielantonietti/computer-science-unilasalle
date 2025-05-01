# resolvedor_bfs.py
from collections import deque

def resolver_labirinto_bfs(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    entrada = saida = None

    for i in range(linhas):
        for j in range(colunas):
            if hasattr(matriz[i][j], 'entrada') and matriz[i][j].entrada:
                entrada = (i, j)
            elif hasattr(matriz[i][j], 'saida') and matriz[i][j].saida:
                saida = (i, j)

    if not entrada or not saida:
        raise ValueError("Entrada ou saída não definidas.")

    fila = deque([entrada])
    visitado = {entrada: None}

    while fila:
        linha, coluna = fila.popleft()

        if (linha, coluna) == saida:
            break

        celula = matriz[linha][coluna]

        vizinhos = []
        if not celula.arestasFechadas.superior:
            vizinhos.append((linha - 1, coluna))
        if not celula.arestasFechadas.inferior:
            vizinhos.append((linha + 1, coluna))
        if not celula.arestasFechadas.esquerda:
            vizinhos.append((linha, coluna - 1))
        if not celula.arestasFechadas.direita:
            vizinhos.append((linha, coluna + 1))

        for viz in vizinhos:
            if viz not in visitado and 0 <= viz[0] < linhas and 0 <= viz[1] < colunas:
                visitado[viz] = (linha, coluna)
                fila.append(viz)

    # Reconstrói o caminho da saída até a entrada
    caminho = []
    atual = saida
    while atual is not None:
        caminho.append(atual)
        atual = visitado[atual]
    caminho.reverse()
    return caminho
