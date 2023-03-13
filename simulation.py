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
    def __init__(self, gui, id):

        self.gui = gui

        if gui: 
            self.physicsClient = p.connect(p.GUI)
            p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
            p.resetDebugVisualizerCamera( cameraDistance=8, cameraYaw=70, cameraPitch=-40, cameraTargetPosition=[0,0,0])



        else:
            self.physicsClient = p.connect(p.DIRECT)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT(id)

    def Run(self):
        for i in range(500):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            if self.gui:
                time.sleep(0.001)

    def Get_Fitness(self, id):
        self.robot.Get_Fitness(id)


    def __del__(self):
        p.disconnect()

                

            