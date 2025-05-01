# 🧭 Maze Creator and Solver Visualizer (DFS & BFS)

Este projeto utiliza o algoritmo de Aldous-Broder para criar um labirinto aleatório e em seguida visualiza a resolução de labirintos utilizando dois algoritmos de busca clássicos:  
**Força Bruta** e **BFS**.  

Os caminhos encontrados por cada algoritmo são exibidos com cores distintas em uma interface gráfica feita com **Pygame**.

## 🎯 Objetivo

Gerar um labirinto com uma entrada e uma saída e posteriormente permitir a comparação visual dos caminhos encontrados pelos algoritmos de busca:
- **Azul**: caminho exclusivo do DFS (Força Bruta Recursiva)
- **Laranja**: caminho exclusivo do BFS
- **Rosa**: caminho compartilhado entre ambos

Além disso, é feita uma comparação de desempenho de cada resolvedor, imprimindo o resultado no terminal.

## 🧠 Algoritmos utilizados

- **Força Bruta** — implementado em `resolvedor.py`
- **BFS** — implementado em `resolvedor_bfs.py`
- Geração de labirintos com o algoritmo **Aldous-Broder** (em `maze.py`)

## 📁 Estrutura do Projeto
├── maze.py # Interface gráfica, geração do labirinto e execução principal
├── resolvedor.py # Resolução via força bruta
└── resolvedor_bfs.py # Resolução via BFS


## ▶️ Como executar

1. Instale as dependências:
```bash
pip install pygame
```
2. Execute o código principal:
```bash
python maze.py
```
