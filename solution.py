import numpy
import pyrosim.pyrosim as pyrosim
import random
from simulate import Simulate


class SOLUTION:
    def __init__(self, id):
        self.bodyLength = random.randint(3, 8)
        self.numLeft = random.randint(1, 5)
        self.numRight = random.randint(1,5)
        self.weights = []

        x = numpy.array(range(self.numLeft))
        y = numpy.array(range(self.numRight)) + (3*self.numLeft)

        for currentRow in numpy.concatenate([x, y]):
            for currentColumn in numpy.concatenate([(numpy.array(list(range(self.numLeft*2))) + self.numLeft), ((3*self.numLeft+self.numRight)+numpy.array(list(range(self.numRight*2))))]):
                self.weights.append(random.random() * 2 - 1)

        self.id = id

    def Evaluate(self, gui):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        Simulate(gui, self.id)
        with open('./fitness/fitness'+ str(self.id) +'.txt', 'r') as file:
            self.fitness = float(file.read())

    def Mutate(self):
        i = random.randint(0,len(self.weights)-1)

        self.weights[i] = random.random() * 2 - 1

    def Set_Id(self, id):
        self.id = id

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        # length = 1
        # width = 1
        # height = 1

        # x = -1
        # y = 1
        # z = 0.5

        # pyrosim.Send_Cube(name="box", pos=[x,y,z] , size=[length,width,height])


        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("./bodies/body" + str(self.id) + ".urdf")


        pyrosim.Send_Cube(name="m", pos=[0,0,1] , size=[1,self.bodyLength,0.5])


        intervalLeft = (float(self.bodyLength)+1) / self.numLeft

        for i in range(self.numLeft):
            pyrosim.Send_Joint(name = "m_L" + str(i) , parent= "m" , child = "L" + str(i) , type = "revolute", position = [-0.5,-1*self.bodyLength/2 + i * intervalLeft,1], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="L" + str(i), pos= [-0.5,0,0], size=[1,0.2,0.2])

            pyrosim.Send_Joint(name = "L" +str(i)+ "_LL" + str(i) , parent= "L" + str(i) , child = "LL" + str(i) , type = "revolute", position = [-1,0,0], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="LL" + str(i), pos= [0,0,-0.5], size=[0.2,0.2,1])

        intervalRight = (float(self.bodyLength)+1) / self.numRight

        for i in range(self.numRight):
            pyrosim.Send_Joint(name = "m_r" + str(i) , parent= "m" , child = "r" + str(i) , type = "revolute", position = [0.5,-1*self.bodyLength/2 + i * intervalRight,1], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="r" + str(i), pos= [0.5,0,0], size=[1,0.2,0.2])

            pyrosim.Send_Joint(name = "r" +str(i)+ "_rl" + str(i) , parent= "r" + str(i) , child = "rl" + str(i) , type = "revolute", position = [1,0,0], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="rl" + str(i), pos= [0,0,-0.5], size=[0.2,0.2,1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("./brains/brain"+ str(self.id) +".nndf")

        for i in range(self.numLeft):
            pyrosim.Send_Sensor_Neuron(name = i , linkName = "LL" + str(i))
            pyrosim.Send_Motor_Neuron( name = i + self.numLeft , jointName = "m_L" + str(i))
            pyrosim.Send_Motor_Neuron( name = i + 2*self.numLeft , jointName = "L"+str(i)+"_LL" + str(i))


        for i in range(self.numRight):
            j = i + 3*self.numLeft
            pyrosim.Send_Sensor_Neuron(name = j , linkName = "rl" + str(i))
            pyrosim.Send_Motor_Neuron( name = j + self.numRight , jointName = "m_r" + str(i))
            pyrosim.Send_Motor_Neuron( name = j + 2*self.numRight, jointName = "r"+str(i)+"_rl" + str(i))


        x = numpy.array(range(self.numLeft))
        y = numpy.array(range(self.numRight)) + (3*self.numLeft)

        i = 0
        for currentRow in numpy.concatenate([x, y]):
            for currentColumn in numpy.concatenate([(numpy.array(list(range(self.numLeft*2))) + self.numLeft), ((3*self.numLeft+self.numRight)+numpy.array(list(range(self.numRight*2))))]):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn  , weight = self.weights[i] )
                i+=1

        pyrosim.End()