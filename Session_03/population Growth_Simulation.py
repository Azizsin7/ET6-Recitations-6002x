import matplotlib.pyplot as plt
import random

def simulate_population_growth(initial_population, num_generations, reproduction_probability):
    """
    Simulates population growth over multiple generations with a stochastic process.

    Parameters:
    - initial_population (int): The initial size of the population.
    - num_generations (int): The number of generations to simulate.
    - reproduction_probability (float): The probability of an individual reproducing in each generation.

    Returns:
    - list: List containing the population size for each generation.
    """
     # Initialize the population with the given initial size
    population = [initial_population]

    # Iterate over each generation
    for i in range(num_generations):
        new_population = 0

        # Simulate reproduction for each individual in the current generation
        for j in range(population[-1]):
            # Check if the individual reproduces based on the given probability
            if random.uniform(0, 1) < reproduction_probability:
                new_population += 1 # Increment the count of reproducing individuals

        # Update the population for the next generation
        population.append(new_population)

    return population

def plot_population_growth(population):
    """
    Plots the population growth over generations.

    Parameters:
    - population (list): List containing the population size for each generation.
    """
    generations = range(len(population))
    plt.plot(generations, population, marker='o')
    plt.xlabel('Generation')
    plt.ylabel('Population Size')
    plt.title('Stochastic Population Growth')
    plt.show()

# Parameters
initial_population = 5
num_generations = 20
reproduction_probability = 0.8

# Simulate population growth
population_history = simulate_population_growth(initial_population, num_generations, reproduction_probability)
print(population_history)
# Plot the results
plot_population_growth(population_history)
