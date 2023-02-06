import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self, id):
        self.robotId = p.loadURDF("./bodies/body" + str(id) + ".urdf")

        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        self.nn = NEURAL_NETWORK("./brains/brain" + str(id) + ".nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                self.motors[bytes(jointName,'UTF-8')].Set_Value(self.robotId, desiredAngle)


    def Think(self):
        self.nn.Update()

    def Get_Fitness(self, id):
        print("getting fitness")
        with open('./fitness/fitness' + str(id) + '.txt', 'w') as file:
            file.write(str( p.getBasePositionAndOrientation(self.robotId)[0][0]))

