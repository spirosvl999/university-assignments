import random

# Αρχικοποίηση του γράφου
graph = {
    '1': ['2', '3'],
    '2': ['1', '3', '4'],
    '3': ['1', '2', '4', '5'],
    '4': ['2', '3', '5', '6'],
    '5': ['3', '4', '6'],
    '6': ['4', '5']
}

def evaluate_fitness(individual, graph):
    fitness = 0
    
    for node, color in individual.items():
        neighbors = graph[node]
        for neighbor in neighbors:
            if individual[neighbor] != color:
                fitness -= 1
    
    return fitness


def selection(population, graph, k):
    # Επιλογή k ατόμων βάσει της καταλληλότητας (του fitness)
    fitness_scores = [evaluate_fitness(individual, graph) for individual in population]
    selected_population = random.choices(population, weights=fitness_scores, k=k)
    return selected_population


def crossover(parent1, parent2):
    # Διασταύρωση ενός σημείου
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = {}
    child2 = {}
    
    for i, (gene1, gene2) in enumerate(zip(parent1.items(), parent2.items())):
        key1, value1 = gene1
        key2, value2 = gene2
        if i < crossover_point:
            child1[key1] = value1
            child2[key2] = value2
        else:
            child1[key1] = value2
            child2[key2] = value1
    
    return child1, child2


def mutate(individual, colors):
    # Μετάλλαξη ενός ψηφίου
    mutated_individual = individual.copy()
    node = random.choice(list(mutated_individual.keys()))
    mutated_individual[node] = random.choice(colors)
    return mutated_individual

# Παράμετροι
population_size = 50
max_generations = 100
mutation_rate = 0.1
replacement_rate = 0.3

colors = ['blue', 'red', 'green', 'yellow']

# Αρχικός πληθυσμός
population = []
for _ in range(population_size):
    individual = {}
    for node in graph.keys():
        individual[node] = random.choice(colors)
    population.append(individual)

# Εξέλιξη πληθυσμού
for generation in range(max_generations):
    # Αξιολόγηση καταλληλότητας
    fitness_scores = [evaluate_fitness(individual, graph) for individual in population]
    best_individual = population[fitness_scores.index(max(fitness_scores))]
    
    # Εκτύπωση καλύτερου αποτελέσματος ανά γενιά
    print(f"Generation {generation + 1} - Best Fitness: {max(fitness_scores)}")
    
    # Επιλογή γονέων
    selected_parents = selection(population, graph, k=int((1 - replacement_rate) * population_size))
    
    # Δημιουργία απογόνων με διασταύρωση
    offspring = []
    for i in range(int(replacement_rate * population_size)):
        parent1, parent2 = random.choices(selected_parents, k=2)
        child1, child2 = crossover(parent1, parent2)
        offspring.extend([child1, child2])
    
    # Μετάλλαξη απογόνων
    for i in range(len(offspring)):
        if random.random() < mutation_rate:
            offspring[i] = mutate(offspring[i], colors)
    
    # Αντικατάσταση πληθυσμού
    population = selected_parents + offspring

# Εκτύπωση του καλύτερου αποτελέσματος
best_fitness = evaluate_fitness(best_individual, graph)
print(f"\nBest Solution: {best_individual}")
print(f"Best Fitness: {best_fitness}")
