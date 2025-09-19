# 🐭 Algoritmo Genético para Encontrar o Caminho do Rato até o Queijo

Este projeto implementa um algoritmo genético para resolver um problema de caminho em um grid bidimensional.
A ideia é simples: um rato precisa sair de um ponto inicial até o queijo, localizado na extremidade oposta da grade, utilizando apenas movimentos limitados.

O algoritmo evolui ao longo das gerações, melhorando os caminhos até encontrar (ou se aproximar) da solução ideal.

# 🚀 Como funciona

O grid é definido como GRID_SIZE x GRID_SIZE (neste caso, 50x50).

O rato sempre começa na primeira coluna (x=0) em uma linha aleatória.

O queijo sempre está na última coluna (x=GRID_SIZE-1) em outra linha aleatória.

Movimentos possíveis:

0 → andar reto (para direita)

1 → subir (para cima)

2 → descer (para baixo)

O algoritmo genético é responsável por:

Gerar população inicial de caminhos (indivíduos).

Avaliar cada caminho com base na distância até o queijo.

Selecionar os melhores (torneio).

Cruzar (crossover) os caminhos para criar novos.

Mutar alguns genes para manter diversidade.

Repetir até atingir o número máximo de gerações ou um caminho ótimo.

# ⚙️ Parâmetros principais

GRID_SIZE = 50 → tamanho do grid

POP_SIZE = 200 → tamanho da população

MAX_GEN = 300 → número máximo de gerações

MUT_RATE = 0.1 → taxa de mutação
