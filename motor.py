import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        amplitude = numpy.pi/4
        frequency = 5
        phaseOffset = 0

        x = numpy.sin(numpy.linspace(0, 2*numpy.pi, 1000))
        self.values = amplitude * numpy.sin(frequency * x + phaseOffset)

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(

        bodyIndex = robot,

        jointName = self.jointName,

        controlMode = p.POSITION_CONTROL,

        targetPosition = self.values[t],

        maxForce = 50)