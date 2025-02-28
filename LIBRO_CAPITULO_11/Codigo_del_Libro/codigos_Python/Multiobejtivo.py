import random
from deap import base, creator, tools, algorithms

# Definir los objetivos y la estructura del individuo
creator.create("FitnessMulti", base.Fitness, weights=(-1.0, 1.0))  # Minimizar el primer objetivo, maximizar el segundo
creator.create("Individual", list, fitness=creator.FitnessMulti)

# Inicializar la caja de herramientas
toolbox = base.Toolbox()

# Definir los atributos del individuo
toolbox.register("attr_float", random.random)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=10)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Definir la función de evaluación
def evaluate(individual):
    obj1 = sum(individual)  # Primer objetivo: minimizar la suma de los valores
    obj2 = sum(x**2 for x in individual)  # Segundo objetivo: maximizar la suma de los cuadrados
    return obj1, obj2

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxSimulatedBinaryBounded, eta=20.0, low=0, up=1)
toolbox.register("mutate", tools.mutPolynomialBounded, eta=20.0, low=0, up=1, indpb=1.0/10)
toolbox.register("select", tools.selNSGA2)

# Configurar el algoritmo evolutivo
def main():
    random.seed(64)
    population = toolbox.population(n=100)
    NGEN = 40
    CXPB = 0.9
    MUTPB = 0.1

    # Evaluar toda la población inicial
    fitnesses = list(map(toolbox.evaluate, population))
    for ind, fit in zip(population, fitnesses):
        ind.fitness.values = fit

    # Evolución de la población
    for gen in range(NGEN):
        offspring = algorithms.varAnd(population, toolbox, CXPB, MUTPB)
        fitnesses = list(map(toolbox.evaluate, offspring))
        for ind, fit in zip(offspring, fitnesses):
            ind.fitness.values = fit
        population = toolbox.select(population + offspring, k=len(population))

    # Obtener los mejores individuos
    best_individuals = tools.selBest(population, k=10)
    for bi in best_individuals:
        print(bi.fitness.values)

if __name__ == "__main__":
    main()