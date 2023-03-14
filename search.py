from generate import Generate
from simulate import Simulate
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import warnings

POPULATION_SIZE = 200
GENERATION_SIZE = 50
K = 10
SHOW_FINAL_CREATURE = True


# Simulate(True, 10)

for i in range(10):
    phc = PARALLEL_HILL_CLIMBER(i, "phc", POPULATION_SIZE, GENERATION_SIZE, gui=SHOW_FINAL_CREATURE)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        phc.Evolve()

for i in range(10):
    phc = PARALLEL_HILL_CLIMBER(i, "TopK", POPULATION_SIZE, GENERATION_SIZE, gui=SHOW_FINAL_CREATURE, topk=K)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        phc.Evolve()

for i in range(10):
    phc = PARALLEL_HILL_CLIMBER(i, "PTK", POPULATION_SIZE, GENERATION_SIZE, gui=SHOW_FINAL_CREATURE)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        phc.Evolve()  

