import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5 #middle of the block at .5 will be ground since it's height is 1

a = 0
b = 1
c = 1.5


pyrosim.Start_SDF("box.sdf")
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
pyrosim.Send_Cube(name="Box2", pos=[a,b,c] , size=[length,width,height])
pyrosim.End()