/*
PROGRAMA: Exercicio 1
AUTOR: Gabriel Antonietti, Bernardo Severo

DESCRIÇÃO:
Este programa implementa e analisa a performance de:
- Busca binaria descrescente em vet ordenado descrescene
- Ordenação utiliando o algoritmo quickSort
- Busca em vet ordenado
- Medição de tempo usando biblioteca tempo.h


- quickSort foi o método de ordenação pois ser amplamente estudado e disparado o mais eficiente
Fonte: https://medium.com/@a.lindemberg/algoritmos-de-ordena%C3%A7%C3%A3o-compara%C3%A7%C3%A3o-797ea0265c4c

- A escolha da busca binária implementada de forma descrescente se deu devido a eficiência do algoritmo e 
a baixa complexidade para realizar a mudança
*/

#include <stdio.h>
#include <stdlib.h>
#include "tempo.h" 
#include "time.h"

// troca o valor dos ponteiros X e Y
void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

// Particiona o vet e retorna o índice final do pivô
int partition(int vet[], int inicio, int fim, long int *comparacoes)
{
    // Seleciona um pivô aleatório (buscando o melhor caso médio)
    // O if evita trocar um elemento por ele mesmo
    int pivo = inicio + (rand() % (fim - inicio + 1));
    if (pivo != fim)
        swap(&vet[pivo], &vet[fim]);
    
    // O valor do pivô é o que está agora no final do vet
    int pivo_valor = vet[fim];
    
    // i marca o início da seção de elementos MAIOR   es ou iguais ao pivô
    int i = inicio;
    int j;
    // Percorre o vet para posicionar os elementos
    for (j = inicio; j < fim; j++)
    {
        (*comparacoes)++;

        // Se o elemento atual for menor ou igual ao pivô
        if (vet[j] <= pivo_valor)
        {
            // swap para a seção dos menores e avança no vet
            swap(&vet[i], &vet[j]);
            i++;
        }
    }
    
    // Posiciona o pivô no índice i
    swap(&vet[i], &vet[fim]);
    
    // Retorna o índice onde o pivô foi colocado
    return i;
}

// Aplica o quickSort de forma recursiva
void quickSort(int vet[], int inicio, int fim, long int *comparacoes)
{
    // Caso base é quando os índices se cruzam
    if (inicio < fim)
    {
        // Particiona o vet e obtém o índice final do pivô
        int pivo = partition(vet, inicio, fim, comparacoes);

        // Aplica o quickSort recursivamente na partição esquerda do pivô
        quickSort(vet, inicio, pivo - 1, comparacoes);

        // Aplica o quickSort recursivamente na partição direita do pivô
        quickSort(vet, pivo + 1, fim, comparacoes);
    }
}


// Realiza uma busca binária em um vetor ordenado de forma decrescente
int buscaBinariaDescendente(int vet[], int tam, int valor, long int *comparacoes) {
    // Define os limites iniciais da busca (o vet inteiro)
    int inicio = 0;
    int fim = tam - 1;
    
    *comparacoes = 0;

    // Continua a busca enquanto inicio é menor que fim
    while (inicio <= fim) {
 
        (*comparacoes)++;
        
        // Calcula o índice do meio do vet
        int meio = inicio + (fim - inicio) / 2;

        // Se o valor no meio é o desejado, returna o valor
        if (vet[meio] == valor) {
            return meio;
        }

        // Se o meio é MENOR, o valor (MAIOR   ) ta na esquerda
        if (vet[meio] < valor) {
            fim = meio - 1;       // Descarta a metade direita do vet
        } 
        // Se o meio é MAIOR   , o vaor (menor) ta na direita
        else {
            inicio = meio + 1;    // Descarta a metade esquerda do vet
        }
    }

    // Se o valor não for encontrado retorna -1
    return -1;
}

// Realiza uma busca binária em um vetor ordenado de forma crescente
int buscaBinaria(int vet[], int tam, int valor, long int *comparacoes) {
    int inicio = 0;
    int fim = tam - 1;
    
    *comparacoes = 0;

    while (inicio <= fim) {

        (*comparacoes)++;
        
        int meio = inicio + (fim - inicio) / 2;

        if (vet[meio] == valor) {
            return meio;
        }

        // Se o meio é MENOR, o valor (MAIOR   ) ta na direita
        if (vet[meio] < valor) {
            inicio = meio + 1;    // Descarta a metade esquerda do vet
        } 
        // Se o meio é MAIOR   , o valor (menor) ta na esquerda
        else {
            fim  = meio - 1;      // Descarta a metade direita do vet
        }
    }

    return -1;
}

int main ()
{   
    srand(time(NULL)); // Semente da aleatoriedade para o quickSort

    int *vet;
    int tam=0, i;
    int valor_a_buscar, posicao;
    long int comparacoes = 0;
     ulong tempo_decorrido;
    
    printf ("Quantos elementos?\n");
    scanf("%d", &tam);
    if (tam <= 0) {
        printf("ERRO tam tem que ser positivo\n");
        return(1);
    }
    vet = (int *) malloc (tam * sizeof(int));
    if (vet == NULL){
        printf("ERRO na alocação de %d elementos\n", tam);
        return(2);
    }

    for (i=0; i<tam; i++) {
        vet[i] = (tam - i) * 2;
    }
    printf("Vetor de %d elementos criado com sucesso\n\n", tam);

    // =================================================================
    // A) Busca em um vetor decrescente 
    // =================================================================
    printf("--- PARTE A: Busca em Vetor Ordenado Decrescente ---\n");
    printf("Digite um valor para buscar no vetor: ");
    scanf("%d", &valor_a_buscar);

    if (valor_a_buscar <= 0) {
        printf("ERRO valor tem que ser positivo\n");
        return(3);
    }
    
    // Utilizando busca binaria descrescente
    printf("Iniciando busca binaria descrescente...\n");
    tempo();
    posicao = buscaBinariaDescendente(vet, tam, valor_a_buscar, &comparacoes);
    tempo_decorrido = tempo();

    if (posicao != -1) {
        printf("\nValor %d encontrado na posicao %d do vetor\n", valor_a_buscar, posicao);
    } else {
        printf("\nERRO Valor %d NAO FOI ENCONTRADO no vetor\n", valor_a_buscar);
    }
    printf("Tempo da busca binaria decrescente: %s\n", formata(tempo_decorrido));
    printf("Numero de comparacoes: %ld\n\n", comparacoes);


    // =================================================================
    // B) Ordenação e nova utilizando busca binaria
    // =================================================================
    printf("--- PARTE B: Ordenacao e Busca em Vetor Ordenado ---\n");
    printf("Ordenando o vetor...\n");

    tempo();

    comparacoes = 0; // Zero comparacoes aqui pois o algoritmo é recursivo

    quickSort(vet, 0, tam - 1, &comparacoes);
    tempo_decorrido = tempo(); 
    
    printf("\nVetor ordenado com sucesso\n");
    printf("Tempo de ordenacao: %s\n\n", formata(tempo_decorrido));
    printf("Numero de comparacoes: %ld\n\n", comparacoes);

    printf("Digite um valor para buscar no vetor JA ORDENADO: ");
    scanf("%d", &valor_a_buscar);

    if (valor_a_buscar <= 0) {
        printf("ERRO valor tem que ser positivo\n");
        return(4);
    }

    printf("Iniciando busca binaria...\n");
    tempo(); 
    posicao = buscaBinaria(vet, tam, valor_a_buscar, &comparacoes);
    tempo_decorrido = tempo();

    if (posicao != -1) {
        printf("\nValor %d encontrado na posicao %d do vetor.\n", valor_a_buscar, posicao);
    } else {
        printf("\nValor %d NAO FOI ENCONTRADO no vetor.\n", valor_a_buscar);
    }
    printf("Tempo da busca binaria: %s\n", formata(tempo_decorrido));
    printf("Numero de comparacoes: %ld\n\n", comparacoes);


    free(vet); 
    return(0); 
}


/*
================================================================================
RELATÓRIO DE ANÁLISE DE PERFORMANCE
================================================================================

METODOLODIA DE TESTES

    CASOS DE TESTE:
        MAIOR   : Busca pelo MAIOR    elemento (valor máximo)
        MEIO: Busca pelo elemento central
        MENOR : Busca pelo MENOR  elemento (valor mínimo)
        INEXISTENTE: Busca por valor que não existe (-999)

    TAMANHO E VALORES:

            | Tamanho (N) | Caso de Teste | Valor Buscado|
            |-------------|---------------|--------------|
            | 100         | MAIOR         | 200          |
            |             | MEIO          | 100          |
            |             | MENOR         | 2            |
            |             | INEXISTENTE   | 0            |
            |-------------|---------------|--------------|
            | 1.000       | MAIOR         | 2000         |
            |             | MEIO          | 1000         |
            |             | MENOR         | 2            |
            |             | INEXISTENTE   | 0            |
            |-------------|---------------|--------------|
            | 5.000       | MAIOR         | 10000        |
            |             | MEIO          | 5000         |
            |             | MENOR         | 2            |
            |             | INEXISTENTE   | 0            |
            |-------------|---------------|--------------|
            | 10.000      | MAIOR         | 20000        |
            |             | MEIO          | 10000        |
            |             | MENOR         | 2            |
            |             | INEXISTENTE   | 0            |
            |-------------|---------------|--------------|
            | 100.000     | MAIOR         | 200000       |
            |             | MEIO          | 100000       |
            |             | MENOR         | 2            |
            |             | INEXISTENTE   | 0            |
    
    COMPARAÇÕES: 

    | Tamanho (N) | Caso de Teste | Comp. Parte A (Desc) | Comp. Parte B (Cresc) |
    |-------------|---------------|----------------------|-----------------------|
    | 100         | MAIOR         | 6                    | 7                     |
    |             | MEIO          | 6                    | 1                     |
    |             | MENOR         | 7                    | 6                     |
    |             | INEXISTENTE   | 7                    | 6                     |
    |-------------|---------------|----------------------|-----------------------|
    | 1.000       | MAIOR         | 9                    | 10                    |
    |             | MEIO          | 9                    | 1                     |
    |             | MENOR         | 10                   | 9                     |
    |             | INEXISTENTE   | 10                   | 9                     |
    |-------------|---------------|----------------------|-----------------------|
    | 5.000       | MAIOR         | 12                   | 13                    |
    |             | MEIO          | 12                   | 1                     |
    |             | MENOR         | 13                   | 12                    |
    |             | INEXISTENTE   | 13                   | 12                    |
    |-------------|---------------|----------------------|-----------------------|
    | 10.000      | MAIOR         | 13                   | 14                    |
    |             | MEIO          | 13                   | 1                     |
    |             | MENOR         | 14                   | 13                    |
    |             | INEXISTENTE   | 14                   | 13                    |
    |-------------|---------------|----------------------|-----------------------|
    | 100.000     | MAIOR         | 16                   | 17                    |
    |             | MEIO          | 16                   | 1                     |
    |             | MENOR         | 17                   | 16                    |
    |             | INEXISTENTE   | 17                   | 16                    |


---
QUESTÃO 1: Quantos testes (comparações) serão feitos para descobrir que um valor não existe no caso da versão A?
---

---
QUESTÃO 2: E no caso da B? Mudou alguma coisa?
---

---
QUESTÃO 3: Percebe alguma lentidão no algoritmo à medida que o tamanho do vetor aumenta? Tente com 100, 1000, 5000, 10 mil...?
---



REFERÊNCIAS:

https://www.programiz.com/dsa/quick-sort
https://github.com/portfoliocourses/c-example-code/blob/main/quicksort.c 
https://pt.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array

*/