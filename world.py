import pybullet as p
import pyrosim.pyrosim as pyrosim

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")

        pyrosim.Prepare_To_Simulate(self.planeId)

        p.loadSDF("world.sdf")