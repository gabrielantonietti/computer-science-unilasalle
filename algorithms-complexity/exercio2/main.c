#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// -------------------------
// Estrutura da AVL
// -------------------------
typedef struct AVL {
    int m;
    int bal; // fator de balanceamento
    char n[80];
    struct AVL *esq;
    struct AVL *dir;
} AVL;

// -------------------------
// Funções de busca
// -------------------------

AVL* buscaPorNome(AVL *raiz, const char *nome) {
    if (raiz == NULL)
        return NULL;
    
    int cmp = strcmp(nome, raiz->n);
    
    if (cmp == 0)
        return raiz;              // encontrou
    else if (cmp < 0)
        return buscaPorNome(raiz->esq, nome); // vai à esquerda
    else
        return buscaPorNome(raiz->dir, nome); // vai à direita
}

// Busca por valor de m (não é ordenado por m)
AVL* buscaPorM(AVL *raiz, int m) {
    if (raiz == NULL)
        return NULL;

    if (raiz->m == m)
        return raiz;

    AVL *p = buscaPorM(raiz->esq, m);
    if (p != NULL)
        return p;

    return buscaPorM(raiz->dir, m);
}

// -------------------------
// Funções de rotação
// -------------------------

// Rotação simples à direita
AVL* rotacaoDireita(AVL *r) {
    AVL *x = r->esq;
    AVL *temp = x->dir;

    x->dir = r;
    r->esq = temp;

    return x; // nova raiz da subárvore
}

// Rotação simples à esquerda
AVL* rotacaoEsquerda(AVL *r) {
    AVL *x = r->dir;
    AVL *temp = x->esq;

    x->esq = r;
    r->dir = temp;

    return x; // nova raiz da subárvore
}

// Rotação dupla à direita (esquerda-direita)
AVL* rotacaoDuplaDireita(AVL *r) {
    r->esq = rotacaoEsquerda(r->esq);
    return rotacaoDireita(r);
}

// Rotação dupla à esquerda (direita-esquerda)
AVL* rotacaoDuplaEsquerda(AVL *r) {
    r->dir = rotacaoDireita(r->dir);
    return rotacaoEsquerda(r);
}

// -------------------------
// Função auxiliar para criar nós (para testes)
// -------------------------
AVL* criaNo(int m, const char *nome) {
    AVL *novo = (AVL*) malloc(sizeof(AVL));
    if (!novo) {
        printf("Erro de alocação\n");
        exit(1);
    }
    novo->m = m;
    novo->bal = 0;
    strcpy(novo->n, nome);
    novo->esq = novo->dir = NULL;
    return novo;
}

// -------------------------
// Exemplo de uso
// -------------------------
int main() {
    // Monta uma pequena árvore AVL manualmente (ordenada por n)
    AVL *raiz = criaNo(10, "Carlos");
    raiz->esq = criaNo(5, "Ana");
    raiz->dir = criaNo(15, "Marcos");
    raiz->esq->dir = criaNo(8, "Bruno");

    // Busca por nome
    AVL *res = buscaPorNome(raiz, "Bruno");
    if (res)
        printf("Encontrado: %s (m=%d)\n", res->n, res->m);
    else
        printf("Nome não encontrado.\n");

    // Busca por m
    res = buscaPorM(raiz, 15);
    if (res)
        printf("Encontrado m=%d -> %s\n", res->m, res->n);
    else
        printf("m não encontrado.\n");

    return 0;
}
