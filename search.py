from generate import Generate
from simulate import Simulate
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import warnings

# phc = PARALLEL_HILL_CLIMBER(0)
# with warnings.catch_warnings():
#     warnings.simplefilter("ignore")
#     phc.Evolve()  


# phc = PARALLEL_HILL_CLIMBER(1)
# with warnings.catch_warnings():
#     warnings.simplefilter("ignore")
#     phc.Evolve()  


# phc = PARALLEL_HILL_CLIMBER(2)
# with warnings.catch_warnings():
#     warnings.simplefilter("ignore")
#     phc.Evolve()  


# phc = PARALLEL_HILL_CLIMBER(3)
# with warnings.catch_warnings():
#     warnings.simplefilter("ignore")
#     phc.Evolve()  

# phc = PARALLEL_HILL_CLIMBER(4)
# with warnings.catch_warnings():
#     warnings.simplefilter("ignore")
#     phc.Evolve()  

phc = PARALLEL_HILL_CLIMBER(7)
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    phc.Evolve()  



# for i in range(5):
#     Generate()fffesf
#     Simulate()
