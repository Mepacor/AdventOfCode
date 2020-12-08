from Map import *
from Tobbogan import *

localGeology = open("tobbogan_geology.txt", 'r')
geology = localGeology.read().splitlines()

map = Map(geology)
tobbogan = Tobbogan()
slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

treeCounters = []
for slope in slopes:
    treeCounter = 0
    while not map.isOutOfBounds(tobbogan.getYPos()):
        if(map.hasTreeOnLocation(tobbogan.getXPos(), tobbogan.getYPos())):
            treeCounter += 1
        tobbogan.slideDown(slope[0], slope[1])
    treeCounters.append(treeCounter)
    tobbogan.getBackToTop()
    print("Amount of trees encountered in trajectory for slope (", slope[0], slope[1] ,"): ", treeCounter)

answer = 1
for number in treeCounters:
    answer *= number

print("Multiplying all gives the answer: ", answer)
