from solution import SOLUTION
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate(True)
        numberOfGenerations = 100
        for currentGeneration in range(numberOfGenerations):
            self.Evolve_For_One_Generation()
        self.parent.Evaluate(True)

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(False)
        print(str(self.parent.fitness) + ", " + str(self.child.fitness))
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.child.fitness > self.parent.fitness:
            self.parent = self.child