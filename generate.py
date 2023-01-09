import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

for i in range (5):
    y = i
    for i in range (5):
        x = i
        l= 1
        for i in range(10):
            nm = "Box"+str(i)
            pyrosim.Send_Cube(name=nm, pos=[x,y,z+i] , size=[l,l,l])
            l = 0.9 *l



pyrosim.End()