import pybullet as p
import time


physicsClient = p.connect(p.GUI)

for i in range(1000):
    p.stepSimulation()
    print(i) # Print the value of the loop variable
    time.sleep(1/60) # Sleep for 1/60th of a second


p.disconnect()
