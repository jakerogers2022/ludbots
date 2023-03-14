from solution import SOLUTION
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self, i, evolutionMethod, populationSize, genNum, gui = False, topk = 10):
        self.evalMethod = evolutionMethod

        self.xi = i
        self.populationSize = populationSize
        self.numberOfGenerations = genNum
        self.topK = topk
        self.parents = {}
        self.children = {}
        self.nextId = 0
        self.gui = gui
        for i in range(self.populationSize):
            self.parents[i] = SOLUTION(self.nextId)
            self.nextId += 1

    def Evolve(self):
        for i in self.parents:
            self.parents[i].Evaluate(False)
        numberOfGenerations = self.numberOfGenerations
        for currentGeneration in range(numberOfGenerations):
            print("------------------------------------------" + str(currentGeneration))

            if self.evalMethod == "phc":
                ps = []
                for gen in self.parents:
                    ps.append(self.parents[gen])

                ps.sort(key=lambda x: x.fitness, reverse=True)
                with open("fitnessDataPHCxx"+str(self.xi), "a") as f:
                    f.write(str(ps[0].fitness)+",")

                for i in range(self.populationSize):
                    self.Evolve_For_One_Generation(i, self.parents[i])

            elif self.evalMethod =='TopK':
                ps = []
                for gen in self.parents:
                    ps.append(self.parents[gen])

                ps.sort(key=lambda x: x.fitness, reverse=True)
                with open("fitnessDataTKxx"+str(self.xi), "a") as f:
                    f.write(str(ps[0].fitness)+",")

                topK = self.topK
                for i in range(int(self.populationSize/topK)):
                    for k in range(topK):
                        self.Evolve_For_One_Generation(i + k * int(self.populationSize/topK), ps[k])
            else:
                ps = []
                ps2 = []
                for gen in self.parents:
                    ps.append(self.parents[gen])
                    ps2.append(self.parents[gen])

                ps2.sort(key=lambda x: x.fitness, reverse=True)
                with open("fitnessDataPTKxx"+str(self.xi), "a") as f:
                    f.write(str(ps2[0].fitness)+",")

                section_size = int(self.populationSize / 10)

                for section in range(10):
                    start_index = section * section_size
                    end_index = (section + 1) * section_size
                    section_ps = ps[start_index:end_index]

                    section_ps.sort(key=lambda x: x.fitness, reverse=True)

                    for i in range(section_size):
                        index = i + start_index 
                        self.Evolve_For_One_Generation(index, section_ps[0])



        if self.gui:
            mx = []
            for i in self.parents:
                mx.append(self.parents[i])

            section_size = int(self.populationSize / 4)

            mx.sort(key=lambda x: x.fitness, reverse=True)

            mx[i].Evaluate(True)

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