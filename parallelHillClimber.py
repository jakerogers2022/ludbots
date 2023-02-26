from solution import SOLUTION
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self, i):
        self.xi = i
        self.populationSize = 1000
        self.parents = {}
        self.children = {}
        self.nextId = 0
        for i in range(self.populationSize):
            self.parents[i] = SOLUTION(self.nextId)
            self.nextId += 1

    def Evolve(self):
        for i in self.parents:
            self.parents[i].Evaluate(False)
        numberOfGenerations = 100
        for currentGeneration in range(numberOfGenerations):
            print("------------------------------------------" + str(currentGeneration))
            ps = []
            for gen in self.parents:
                ps.append(self.parents[gen])

            ps.sort(key=lambda x: x.fitness, reverse=True)
            with open("fitnessData"+str(self.xi), "a") as f:
                f.write(str(ps[0].fitness)+",")

            topK = 10
            for i in range(int(self.populationSize/topK)):
                for k in range(topK):
                    self.Evolve_For_One_Generation(i + k * int(self.populationSize/topK), ps[0])

                # self.Evolve_For_One_Generation(i, ps[0])
                # self.Evolve_For_One_Generation(int(self.populationSize/4)+1, ps[1])
                # self.Evolve_For_One_Generation(int(2*self.populationSize/4)+1, ps[2])
                # self.Evolve_For_One_Generation(int(3*self.populationSize/4)+1, ps[3])
            # for i in range(self.populationSize):
            #     self.Evolve_For_One_Generation(i, ps[i])
                
        mx = -999
        for i in self.parents:
            mx = max(mx, self.parents[i].fitness)

        for i in self.parents:
            if self.parents[i].fitness == mx: 
                print(i)
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