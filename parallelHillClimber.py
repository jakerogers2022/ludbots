from solution import SOLUTION
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.populationSize = 40
        self.parents = {}
        self.children = {}
        self.nextId = 0
        for i in range(self.populationSize):
            self.parents[i] = SOLUTION(self.nextId)
            self.nextId += 1

    def Evolve(self):
        for i in self.parents:
            self.parents[i].Evaluate(False)
        numberOfGenerations = 50
        for currentGeneration in range(numberOfGenerations):
            print("------------------------------------------" + str(currentGeneration))
            ps = []
            for gen in self.parents:
                ps.append(self.parents[gen])

            ps.sort(key=lambda x: x.fitness, reverse=True)
            for i in range(int(self.populationSize/4)):
                self.Evolve_For_One_Generation(i, ps[0])
                self.Evolve_For_One_Generation(int(self.populationSize/4)+1, ps[1])
                self.Evolve_For_One_Generation(int(2*self.populationSize/4)+1, ps[2])
                self.Evolve_For_One_Generation(int(3*self.populationSize/4)+1, ps[3])
                
        mx = -999
        for i in self.parents:
            mx = max(mx, self.parents[i].fitness)

        for i in self.parents:
            if self.parents[i].fitness == mx: 
                x = input("prompt")
                self.parents[i].Evaluate(True)

    def Evolve_For_One_Generation(self, id, parent):
        self.Spawn(id, parent)
        self.Mutate(id)
        self.children[id].Evaluate(False)

        print("Parents Fitness: " + str(parent.fitness) + ", Child's Fitness: " + str(self.children[id].fitness))
        self.Select(id)

    def Spawn(self, id, parent):
        self.children[id] = copy.deepcopy(parent)
        self.children[id].id = id

    def Mutate(self,id):
        self.children[id].Mutate()

    def Select(self, id):
        if abs(self.children[id].fitness) > abs(self.parents[id].fitness):
            self.parents[id] = self.children[id]