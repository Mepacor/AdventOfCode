# Map class that contains the geology of the slope
class Map(object):
    def __init__(self, map):
        self.map = map
        self.patternSize = len(map[0])
    
    def hasTreeOnLocation(self, xPos, yPos):
        return self.map[yPos][xPos % self.patternSize] == "#"

    def isOutOfBounds(self, yPos):
        return yPos > len(self.map)-1