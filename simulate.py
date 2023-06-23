import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8) #adds gravity

planeId = p.loadURDF("plane.urdf") #adds floor

p.loadSDF("box.sdf") #adds box

for i in range(1000):
    p.stepSimulation()
    print(i) # Print the value of the loop variable
    time.sleep(1/60) # Sleep for 1/60th of a second


p.disconnect()
