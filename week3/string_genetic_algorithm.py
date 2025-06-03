import random
import string

class GeneticAlgorithm:
    def __init__(self, target: str, population_size: int = 10):
        self.target = target.upper()
        self.population_size = population_size
        self.population = []
        self.__initialise_population()

    def __initialise_population(self):
        """
        Create the initial population of random strings (chromosomes)
        with the same length as the target string.
        """
        for _ in range(self.population_size):
            chromosome = ''.join(random.choices(string.ascii_uppercase, k=len(self.target)))
            self.population.append(chromosome)

    def display_population(self):
        for i, chromosome in enumerate(self.population, start=1):
            print(f"Chromosome {i}: {chromosome}")

# Example usage
if __name__ == "__main__":
    ga = GeneticAlgorithm("HELLO", population_size=5)
    ga.display_population()

