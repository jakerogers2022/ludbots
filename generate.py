import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    length = 1
    width = 1
    height = 1

    x = -1
    y = 1
    z = 0.5

    pyrosim.Send_Cube(name="box", pos=[x,y,z] , size=[length,width,height])


    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    length = 1
    width = 1
    height = 1

    x = 0
    y = 0
    z = 0.5

    pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[length,width,height])
    pyrosim.Send_Cube(name="Leg", pos= [1.0,0,1.5], size=[length,width,height])
    pyrosim.Send_Joint(name = "Torso_Leg" , parent= "Torso" , child = "Leg" , type = "revolute", position = [0.5,0.5,0.5])
    pyrosim.End()

Create_World()
Create_Robot()