from world import WORLD
from robot import ROBOT

import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c

class SIMULATION:
    def __init__(self, gui):

        self.gui = gui

        if gui: 
            self.physicsClient = p.connect(p.GUI)

        else:
            self.physicsClient = p.connect(p.DIRECT)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(500):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            if self.gui:
                time.sleep(0.001)

    def Get_Fitness(self):
        self.robot.Get_Fitness()


    def __del__(self):
        p.disconnect()

                

            