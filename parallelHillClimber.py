from solution import SOLUTION
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        populationSize = 10
        self.parents = {}
        self.children = {}
        self.nextId = 0
        for i in range(populationSize):
            self.parents[i] = SOLUTION(self.nextId)
            self.nextId += 1

    def Evolve(self):
        for i in self.parents:
            self.parents[i].Evaluate(False)
        numberOfGenerations = 10
        for currentGeneration in range(numberOfGenerations):
            self.Evolve_For_One_Generation()
        
        mx = -999
        for i in self.parents:
            mx = max(mx, self.parents[i].fitness)

        for i in self.parents:
            if self.parents[i].fitness == mx: 
                self.parents[i].Evaluate(True)

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        for i in self.parents:
            self.children[i].Evaluate(False)

        for i in self.parents:
            print("Parents Fitness: " + str(self.parents[i].fitness) + ", Child's Fitness: " + str(self.children[i].fitness))
        self.Select()

    def Spawn(self):
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_Id(self.nextId)
            self.nextId += 1

    def Mutate(self):
        for i in self.parents:
            self.children[i].Mutate()

    def Select(self):
        for i in self.parents:
            if self.children[i].fitness > self.parents[i].fitness:
                self.parents[i] = self.children[i]