import random
import numpy as np

# Configuração do ambiente
GRID_SIZE = 50
POP_SIZE = 200
MAX_GEN = 300
MUT_RATE = 0.1

# Posições iniciais e finais fixas durante toda a execução
start_y = random.randint(0, GRID_SIZE - 1)
end_y = random.randint(0, GRID_SIZE - 1)
start = (start_y, 0)
goal = (end_y, GRID_SIZE - 1)

# Movimentos possíveis: 0 = reto, 1 = subir, 2 = descer
MOVES = [0, 1, 2]

def generate_individual():
    """Gera um caminho aleatório até a última coluna."""
    return [random.choice(MOVES) for _ in range(GRID_SIZE - 1)]

def simulate_path(individual):
    """Executa o caminho e retorna distância percorrida."""
    y, x = start
    path_length = 0
    
    for move in individual:
        # sempre anda para frente (direita)
        x += 1
        if move == 1:  # subir
            y -= 1
        elif move == 2:  # descer
            y += 1

        # Penaliza caso saia do grid
        if y < 0 or y >= GRID_SIZE:
            return 9999  # caminho inválido grande custo

        path_length += 1

        # chegou ao queijo
        if (y, x) == goal:
            return path_length

    # penaliza se não chegar
    return path_length + abs(goal[0] - y) + abs(goal[1] - x)

def fitness(individual):
    """Quanto menor a distância, maior o fitness."""
    dist = simulate_path(individual)
    return 1 / (1 + dist)

def tournament_selection(pop, k=3):
    """Seleciona melhor de k indivíduos."""
    selected = random.sample(pop, k)
    return max(selected, key=lambda ind: fitness(ind))

def crossover(p1, p2):
    """Cruzamento de ponto único."""
    point = random.randint(1, len(p1) - 1)
    return p1[:point] + p2[point:], p2[:point] + p1[point:]

def mutate(ind):
    """Mutação aleatória."""
    for i in range(len(ind)):
        if random.random() < MUT_RATE:
            ind[i] = random.choice(MOVES)
    return ind

# Inicializa população
population = [generate_individual() for _ in range(POP_SIZE)]

# Loop evolutivo
best_path = None
best_fitness = 0

for gen in range(MAX_GEN):
    new_population = []
    for _ in range(POP_SIZE // 2):
        p1 = tournament_selection(population)
        p2 = tournament_selection(population)
        child1, child2 = crossover(p1, p2)
        new_population.append(mutate(child1))
        new_population.append(mutate(child2))

    population = new_population

    # Avalia melhor indivíduo
    for ind in population:
        fit = fitness(ind)
        if fit > best_fitness:
            best_fitness = fit
            best_path = ind

    if gen % 20 == 0:
        print(f"Geração {gen} | Melhor Fitness: {best_fitness:.4f} | Distância: {simulate_path(best_path)}")

# Resultado final
print("\nMelhor caminho encontrado:")
print(best_path)
print(f"Distância total: {simulate_path(best_path)}")
print(f"Rato começa em {start} e queijo em {goal}")
