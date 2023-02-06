from simulation import SIMULATION

def Simulate(gui, id):
    simulation = SIMULATION(gui, id)

    simulation.Run()
    simulation.Get_Fitness(id)

# import pybullet as p
# import time
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import numpy
# import random
# import constants as c


# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())

# p.setGravity(0,0,-9.8)

# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")


# p.loadSDF("world.sdf")

# pyrosim.Prepare_To_Simulate(robotId)

# backLegSensorValues = numpy.zeros(1000)
# frontLegSensorValues = numpy.zeros(1000)

# amplitude = numpy.pi/4
# frequency = 5
# phaseOffset = 0

# x = numpy.sin(numpy.linspace(0, 2*numpy.pi, 1000))

# x = amplitude * numpy.sin(frequency * x + phaseOffset)

# phaseOffset2 = 0.5

# x2 = amplitude * numpy.sin(20 * x + phaseOffset2)

# for i in range(1000):
#     pyrosim.Set_Motor_For_Joint(

#     bodyIndex = robotId,

#     jointName = b'Torso_BackLeg',

#     controlMode = p.POSITION_CONTROL,

#     targetPosition = x[i],

#     maxForce = 50)

#     pyrosim.Set_Motor_For_Joint(

#     bodyIndex = robotId,

#     jointName = b'Torso_FrontLeg',

#     controlMode = p.POSITION_CONTROL,

#     targetPosition = x2[i],

#     maxForce = 50)

#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

#     time.sleep(0.001)

# with open('data/data.npy', 'wb') as f:
#     numpy.save(f,backLegSensorValues)

# with open('data/data2.npy', 'wb') as f:
#     numpy.save(f,frontLegSensorValues)

# p.disconnect()