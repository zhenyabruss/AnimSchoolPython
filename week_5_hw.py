import maya.cmds as cmds
import math

class Rocket:

    buildOffsetY = 0 # parts of rocket building height offset

    def __init__(self, bodyParts = 4, noseConeHeight = 10, fuelTanks = 4, bodyRadius = 3, bodyHeight = 5):
        self.bodyParts = bodyParts
        self.noseConeHeight = noseConeHeight
        self.fuelTanks = fuelTanks
        self.bodyRadius = bodyRadius
        self.bodyHeight = bodyHeight

    def generateFuelTank(self, bodyRadius, fuelTanks, coneHeight ):
        
        self.buildOffsetY = coneHeight + coneHeight / 2 

        # zero cone check
        if fuelTanks <= 0:
            cmds.error("Number of cones should be greater than zero")
            return
        
        # create cones in raw
        angle_increment = 360.0 / fuelTanks
        for i in range(fuelTanks):
            angle = math.radians(i * angle_increment)
            x = bodyRadius * math.cos(angle)
            z = bodyRadius * math.sin(angle)
            cmds.polyCone(radius=1, height=coneHeight) 
            cmds.move(x, coneHeight/2 , z)
        
        


    def generateBody(self):
        for i in range(self.bodyParts):
            body = cmds.polyCylinder(n="body", height= self.bodyHeight,  r = self.bodyRadius)
            cmds.xform (body, t = [0, self.buildOffsetY, 0], r=1)
            self.buildOffsetY = self.buildOffsetY + self.bodyHeight


    def generateNose (self):
        
        self.buildOffsetY = self.buildOffsetY - self.bodyHeight / 2 + self.noseConeHeight / 2

        nose = cmds.polyCone(height=self.noseConeHeight, radius = self.bodyRadius)
        cmds.xform(nose,t=[0,self.buildOffsetY,0], ws=True)
    
        


    def generateModel(self):
        self.generateFuelTank (bodyRadius = 3, fuelTanks = 6, coneHeight = 3)
        self.generateBody()
        self.generateNose()






        

myRocket = Rocket (bodyParts = 4, noseConeHeight = 10, fuelTanks = 4, bodyRadius = 3)
myRocket.generateModel() 