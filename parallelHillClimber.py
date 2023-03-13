from solution import SOLUTION
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self, i, evolutionMethod):
        self.evalMethod = evolutionMethod

        self.xi = i
        self.populationSize = 200
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

            if self.evalMethod == "phc":
                ps = []
                for gen in self.parents:
                    ps.append(self.parents[gen])

                ps.sort(key=lambda x: x.fitness, reverse=True)
                with open("fitnessDataPHC"+str(self.xi), "a") as f:
                    f.write(str(ps[0].fitness)+",")

                for i in range(self.populationSize):
                    self.Evolve_For_One_Generation(i, self.parents[i])

            elif self.evalMethod =='TopK':
                ps = []
                for gen in self.parents:
                    ps.append(self.parents[gen])

                ps.sort(key=lambda x: x.fitness, reverse=True)
                with open("fitnessDataTK"+str(self.xi), "a") as f:
                    f.write(str(ps[0].fitness)+",")

                topK = 10
                for i in range(int(self.populationSize/topK)):
                    for k in range(topK):
                        self.Evolve_For_One_Generation(i + k * int(self.populationSize/topK), ps[k])
            else:
                ps = []
                for gen in self.parents:
                    ps.append(self.parents[gen])

                with open("fitnessDataPTK"+str(self.xi), "a") as f:
                    f.write(str(ps[0].fitness)+",")

                section_size = int(self.populationSize / 10)

                for section in range(10):
                    start_index = section * section_size
                    end_index = (section + 1) * section_size
                    section_ps = ps[start_index:end_index]

                    section_ps.sort(key=lambda x: x.fitness, reverse=True)

                    for i in range(section_size):
                        index = i + start_index 
                        self.Evolve_For_One_Generation(index, section_ps[0])


                # self.Evolve_For_One_Generation(i, ps[0])
                # self.Evolve_For_One_Generation(int(self.populationSize/4)+1, ps[1])
                # self.Evolve_For_One_Generation(int(2*self.populationSize/4)+1, ps[2])
                # self.Evolve_For_One_Generation(int(3*self.populationSize/4)+1, ps[3])

                
        # mx = []
        # for i in self.parents:
        #     mx.append(self.parents[i])

        # section_size = int(self.populationSize / 4)

        # for section in range(4):
        #     start_index = section * section_size
        #     end_index = (section + 1) * section_size
        #     section_ps = mx[start_index:end_index]

        #     section_ps.sort(key=lambda x: x.fitness, reverse=True)
        #     x = input("prompt")
        #     section_ps[0].Evaluate(True)

        # mx.sort(key=lambda x: x.fitness, reverse=True)

        # for i in range(5):
        #     print(i)
        #     x = input("prompt")
        #     mx[i].Evaluate(True)

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