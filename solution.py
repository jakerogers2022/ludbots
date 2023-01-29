import numpy
import pyrosim.pyrosim as pyrosim
import random
from simulate import Simulate


class SOLUTION:
    def __init__(self, id):
        self.weights = numpy.random.rand(4, 8) * 2 - 1
        self.id = id

    def Evaluate(self, gui):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        Simulate(gui, self.id)
        with open('fitness'+ str(self.id) +'.txt', 'r') as file:
            self.fitness = float(file.read())

    def Mutate(self):
        row = random.randint(0,2)
        col = random.randint(0,7)

        self.weights[row][col] = random.random() * 2 - 1

    def Set_Id(self, id):
        self.id = id

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        length = 1
        width = 1
        height = 1

        x = -1
        y = 1
        z = 0.5

        pyrosim.Send_Cube(name="box", pos=[x,y,z] , size=[length,width,height])


        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        length = 1
        width = 1
        height = 1

        x = 1.5
        y = 0
        z = 1.5

        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[length,width,height])
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos= [0,-0.5,0], size=[0.2,1,0.2])
        pyrosim.Send_Cube(name="FrontLeg", pos= [0,0.5,0], size=[0.2,1,0.2])

        pyrosim.Send_Joint(name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0,1], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightLeg", pos= [0.5,0,0], size=[1,0.2,0.2])
        pyrosim.Send_Cube(name="LeftLeg", pos= [-0.5,0,0], size=[1,0.2,0.2])

        pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos= [0,0,-0.5], size=[0.2,0.2,1])
        pyrosim.Send_Cube(name="FrontLowerLeg", pos= [0,0,-0.5], size=[0.2,0.2,1])

        pyrosim.Send_Joint(name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos= [0,0,-0.5], size=[0.2,0.2,1])
        pyrosim.Send_Cube(name="LeftLowerLeg", pos= [0,0,-0.5], size=[0.2,0.2,1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+ str(self.id) +".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "RightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLowerLeg")

        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "RightLeg_RightLowerLeg")

        for currentRow in [0,1,2,3]:
            for currentColumn in [0,1,2,3,4,5,6,7]:
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + 4  , weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()