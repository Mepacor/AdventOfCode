# Tobbogan class that can move and holds its current position
class Tobbogan(object):
    def __init__(self):
        self.xPos = 0
        self.yPos = 0

    def getXPos(self):
        return self.xPos
    
    def getYPos(self):
        return self.yPos

    def slideDown(self, stepsRight, stepsDown):
        self.xPos += stepsRight
        self.yPos += stepsDown

    def getBackToTop(self):
        self.xPos = 0
        self.yPos = 0