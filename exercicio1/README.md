# Atividade em C - Vetores Dinâmicos, Busca e Ordenação

## 📌 Descrição
Este programa em **C** trabalha com **vetores dinâmicos** alocados via `malloc`.  
Ele gera automaticamente um vetor de inteiros pares em ordem **decrescente**, com base no tamanho informado pelo usuário, e depois realiza operações de **busca** e **ordenação**.

---

## 🚀 Objetivos
1. Perguntar ao usuário **quantos elementos** deseja criar.
2. Criar dinamicamente um vetor com números **pares não ordenados**:
   - Exemplo (tam = 5):
     ```
     vet[0] = 10
     vet[1] = 8
     vet[2] = 6
     vet[3] = 4
     vet[4] = 2
     ```
   - Fórmula usada:
     ```c
     vet[i] = (tam - i) * 2;
     ```
3. Solicitar um valor e **buscar no vetor** (versão não ordenada).
4. Implementar um **algoritmo de ordenação manual** (sem usar funções prontas da linguagem).
5. Repetir a busca no vetor já ordenado.
6. Analisar e comentar os resultados de desempenho.

---

## 📝 Questões a serem respondidas
- **A)** Quantos testes serão feitos para descobrir que um valor não existe na versão A (vetor não ordenado)?
- **B)** Quantos testes serão feitos para descobrir que um valor não existe na versão B (vetor ordenado)?
- **C)** Houve diferença de desempenho entre A e B?
- **D)** Houve lentidão perceptível ao aumentar o tamanho do vetor (100, 1.000, 5.000, 10.000 elementos)?

---

## 📂 Estrutura do Código
O programa segue a seguinte estrutura:
1. Entrada do tamanho (`scanf`).
2. Criação dinâmica do vetor (`malloc`).
3. Alimentação do vetor com números pares em ordem decrescente.
4. **Parte A:** busca sequencial.
5. Ordenação (ex.: Bubble Sort, Insertion Sort ou Selection Sort).
6. **Parte B:** busca novamente após ordenação.
7. Relatório dos testes como comentários no final do código.

---
