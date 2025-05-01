def resolver_labirinto(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    print("oi")
    # Localiza entrada e saída
    entrada = saida = None
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j].entrada:
                entrada = (i, j)
            elif matriz[i][j].saida:
                saida = (i, j)

    if not entrada or not saida:
        raise ValueError("Entrada ou saída não definidas.")

    linha_entrada, coluna_entrada = entrada
    linha_saida, coluna_saida = saida

    # Inicia a busca
    caminho = busca(matriz, linha_entrada, coluna_entrada, linha_saida, coluna_saida)
    return caminho

def busca(matriz, linha, coluna, linha_saida, coluna_saida):
    if linha < 0 or linha >= len(matriz) or coluna < 0 or coluna >= len(matriz[0]):
        return None

    celula = matriz[linha][coluna]

    if celula.caminho_visitado:
        return None

    celula.caminho_visitado = True  # Marca como parte do caminho

    # Chegou na saída
    if linha == linha_saida and coluna == coluna_saida:
        return [(linha, coluna)]

    # Tenta mover para direções onde não há parede
    if not celula.arestasFechadas.superior:
        caminho = busca(matriz, linha - 1, coluna, linha_saida, coluna_saida)
        if caminho:
            return [(linha, coluna)] + caminho

    if not celula.arestasFechadas.inferior:
        caminho = busca(matriz, linha + 1, coluna, linha_saida, coluna_saida)
        if caminho:
            return [(linha, coluna)] + caminho

    if not celula.arestasFechadas.esquerda:
        caminho = busca(matriz, linha, coluna - 1, linha_saida, coluna_saida)
        if caminho:
            return [(linha, coluna)] + caminho

    if not celula.arestasFechadas.direita:
        caminho = busca(matriz, linha, coluna + 1, linha_saida, coluna_saida)
        if caminho:
            return [(linha, coluna)] + caminho

    # Se nenhuma direção funcionar, desfaz a marcação
    celula.caminho_visitado = False
    return None
