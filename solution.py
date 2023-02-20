import numpy
import pyrosim.pyrosim as pyrosim
import random
from simulate import Simulate
import copy

nodes = []

class Node():

    def __init__(self, bodyPos, absPosRanges, dimensions, name, absBodyPos, depth):
        global nodes
        nodes.append(self)
        self.dimensions= dimensions
        self.sensor = random.random() > 0.5
        self.name = name
        self.absBodyPos = absBodyPos
        self.depth = depth
        self.joints = []

        color = "Green"
        if self.sensor:
            color="Blue"

        pyrosim.Send_Cube(name=name, pos=bodyPos, size=dimensions, color=color)

        jointDirections = ['0 0 1','1 0 0', '0 1 0']
        self.absPosRanges = absPosRanges
        self.children= []  

        hasChildren = random.random() > float(depth)/7
        if hasChildren or depth <= 2:
            self.NumChildren = random.randint(1, 5)
            growDirs = []
            for i in range(self.NumChildren):
            # for i in range(2):
                jointDirection = jointDirections[random.randint(0,2)]

                growAxis = random.randint(0,2)

                if growAxis not in growDirs:

                    growDirs.append(growAxis)

                    # growAxis = 2

                    growDirections = [1, 1]
                    gd = growDirections[random.randint(0, 1)]
                    childJointPosition = copy.deepcopy(bodyPos)
                    childJointPosition[growAxis] += gd * dimensions[growAxis] /2

                    childDimensions = [1,1,1]#numpy.random.rand(1, 3).tolist()[0]
                    childDimensions[growAxis] += random.random()
                    childBodyPos = [0,0,0]
                    childBodyPos[growAxis] += childDimensions[growAxis]/2


                    childAbsPos = self.calcAbsPos(absBodyPos, growAxis, dimensions, childDimensions, gd)

                    childAbsRanges = self.calcAbsRanges(childAbsPos, childDimensions)

                    if self.checkIfNodeIsValid(childAbsRanges):
                        childName = name + str(i)
                        pyrosim.Send_Joint(name = name + "_" + childName, parent=name , child = childName , type = "revolute", position = childJointPosition, jointAxis = jointDirection)
                        self.joints.append(name + "_" + childName)
                        child = Node(childBodyPos, childAbsRanges, childDimensions, childName, childAbsPos, depth+1)
                        self.children.append(child)
                    

    def calcAbsRanges(self, absBodyPos, childDims):
        val = []
        for i in range(3):
            val.append([absBodyPos[i] - childDims[i]/2, absBodyPos[i] + childDims[i]/2])
        return val
    
    def calcAbsPos(self, absBodyPos, growAxis, dims, childDims, growDirection):
        val = copy.deepcopy(absBodyPos)
        val[growAxis] += dims[growAxis]/2 + growDirection * childDims[growAxis]/2
        return val

    def checkIfNodeIsValid(self, childAbsPosRanges):
        for node in nodes:
                x = False
                for i in range(3):
                    if not (node.absPosRanges[i][0] >= min(childAbsPosRanges[i]) and node.absPosRanges[i][0] <= max(childAbsPosRanges[i])):
                        x = True
                if not x:
                    return False

        return True


class SOLUTION:
    def __init__(self, id):
        # self.length = random.randint(5,25)
        # self.body = numpy.random.rand(4, self.length)
        # self.body[:3][:] += 0.1

        # self.body[:3][:] *= 2

        self.body = None

        # # self.body = numpy.ones((4,5))
        # # self.body[0][:] = 3

        
        # self.weights = []
        
        # for i in range(self.length):
        #     if self.body[3][i] > 0.5:
        #         for j in range(self.length, self.length * 2):
        #             self.weights.append(random.random() * 2 - 1)
        #     else:
        #         for j in range(self.length, self.length * 2):
        #             self.weights.append(0)

        # x = numpy.array(range(self.numLeft))
        # y = numpy.array(range(self.numRight)) + (3*self.numLeft)

        # for currentRow in numpy.concatenate([x, y]):
        #     for currentColumn in numpy.concatenate([(numpy.array(list(range(self.numLeft*2))) + self.numLeft), ((3*self.numLeft+self.numRight)+numpy.array(list(range(self.numRight*2))))]):
        #         self.weights.append(random.random() * 2 - 1)

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

        # color = "Green"
        # if self.body[3][0] > 0.5:
        #     color="Blue"

        # pyrosim.Send_Cube(name="Body", pos=[0,0,1] , size=[self.body[0][0], self.body[1][0], self.body[2][0]], color=color)
        # pyrosim.Send_Joint(name = "L0_L1", parent= "L0" , child = "L1" , type = "revolute", position = [0,self.body[1][0]/2,1], jointAxis = "1 0 0")
        body = Node([0,0,0.5],  [[-0.5, 0.5],[-0.5, 0.5],[0, 1]], [1,1,1], "rootLink", [0,0,0.5], 1)

        self.body = body

        global nodes
        nodes = []
        # pyrosim.Send_Joint(name = "L0_L1", parent= "L0" , child = "L1" , type = "revolute", position = [0,self.body[1][0]/2,1], jointAxis = "0 1 0")

        # for i in range(1,len(self.body[0][:])-1):
        #     color = "Green"
        #     if self.body[3][i] > 0.5:
        #         color="Blue"
        #     pyrosim.Send_Cube(name="L" + str(i), pos= [0,self.body[1][i]/2,0],size=[self.body[0][i], self.body[1][i], self.body[2][i]], color=color)
        #     pyrosim.Send_Joint(name = "L" + str(i) + "_L" + str(i+1), parent= "L"+str(i) , child = "L" + str(i+1) , type = "revolute", position = [0,self.body[1][i],0], jointAxis = "1 1 0")
        #     # pyrosim.Send_Joint(name = "L" + str(i) + "_L" + str(i+1) + "S", parent= "L"+str(i) , child = "L" + str(i+1) , type = "revolute", position = [0,self.body[1][i],0], jointAxis = "0 1 0")


        # color = "Green"
        # if self.body[3][len(self.body[0][:])-1] > 0.5:
        #         color="Blue"
        # pyrosim.Send_Cube(name="L" + str(len(self.body[0][:])-1), pos=[0,self.body[1][len(self.body[0][:])-1]/2,0], size=[self.body[0][len(self.body[0][:])-1], self.body[1][len(self.body[0][:])-1], self.body[2][len(self.body[0][:])-1]], color=color)


        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("./brains/brain"+ str(self.id) +".nndf")

        allSensorNames = []
        allJointNames = []

        curNode = self.body
        nodeStack = []


        while True:
            if curNode.sensor:
                allSensorNames.append(curNode.name)
            
            allJointNames.extend(curNode.joints)

            nodeStack.extend(curNode.children)
            if len(nodeStack) == 0:
                break
            else:
                curNode = nodeStack.pop()


        for i in allSensorNames:
            pyrosim.Send_Sensor_Neuron(name = i+"x" , linkName = i)

        for i in allJointNames:
            pyrosim.Send_Motor_Neuron( name = i+"x", jointName = i)


        for i in allSensorNames:
            for j in allJointNames:
                pyrosim.Send_Synapse(sourceNeuronName=i+"x", targetNeuronName=j+"x", weight=random.random() *2-1)



        # for i in range(self.length-1):
        #     if self.body[3][i] < 0.5:
        #         pyrosim.Send_Sensor_Neuron(name = i , linkName = "L" + str(i))
        #     pyrosim.Send_Motor_Neuron( name = i + 2*self.length , jointName = "L"+str(i)+"_L" + str(i+1))


        # for i in range(self.length):
        #     if self.body[3][i] < 0.5:
        #         for j in range(self.length, self.length * 2):
        #             pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j, weight=self.weights[i+j])

        # for i in range(self.numRight):
        #     j = i + 3*self.numLeft
        #     pyrosim.Send_Sensor_Neuron(name = j , linkName = "rl" + str(i))
        #     pyrosim.Send_Motor_Neuron( name = j + self.numRight , jointName = "m_r" + str(i))
        #     pyrosim.Send_Motor_Neuron( name = j + 2*self.numRight, jointName = "r"+str(i)+"_rl" + str(i))


        # x = numpy.array(range(self.numLeft))
        # y = numpy.array(range(self.numRight)) + (3*self.numLeft)

        # i = 0
        # for currentRow in numpy.concatenate([x, y]):
        #     for currentColumn in numpy.concatenate([(numpy.array(list(range(self.numLeft*2))) + self.numLeft), ((3*self.numLeft+self.numRight)+numpy.array(list(range(self.numRight*2))))]):
        #         pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn  , weight = self.weights[i] )
        #         i+=1



        pyrosim.End()