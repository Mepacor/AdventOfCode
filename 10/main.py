# reading and prepping data
adapters = open("adapters.txt", "r").read().splitlines()
adapters = [int(x) for x in adapters]
adapters = [0] + sorted(adapters) # adding 0 in front
adapters.append(adapters[-1]+3) # adding max+3 at the end

# Part one: multiply the number of 1 and 3 differences
# using a frequency table to keep track of the differences
freqTable = [0,0,0] # amount of 1, 2 and 3 jolt differences
for i in range(0, len(adapters)-1):
    index = adapters[i+1] - adapters[i] - 1
    freqTable[index] += 1

print("Day 10 - part one: multiplying amount of 1 and 3 differences gives:", freqTable[0]*freqTable[2])
print("Frequency table of respectively 1, 2, and 3 jolt difference between adapters:", freqTable)


# part 2: calculating the amount of possible adapter configurations
# general idea when current node [6] can jump to two other nodes [7,8] : #branches[6] = #branches[7] + #branches[8]
def getNumberOfPossibilitiesForEachNode(iterator): # calculates if a adapter (=node) has 1, 2 or 3 possible ways to be connected with another adapter
    count = 0
    for index in range(iterator+1, len(adapters)):
        if(adapters[index]-adapters[iterator] <= 3):
            count += 1
        else:
            break
    return count

def getNumberOfPossibilitiesForAllNodes(data): # gives a list of with the possibilities for all nodes (1, 2 or 3) 
    listOfPossibilities = []
    for index in range(0, len(data)-1):
        listOfPossibilities.append(getNumberOfPossibilitiesForEachNode(index))
    return listOfPossibilities

def getNumberOfCombinationsFor(listOfPossibilities): # calculates for each node, how many branches there are beneath itself, and saves it in a dictionary
    indexDict = {len(listOfPossibilities)-1 : 1} # last adapter has only 1 possible branch
    for index in range(len(listOfPossibilities)-2, -1, -1):
        count = 0
        for idxNextNode in range(0, listOfPossibilities[index]):
            count += indexDict[index+idxNextNode+1] #f.e. indexDict[47] = indexDict[48] + indexDict[49] = 2
        indexDict[index] = count
    return indexDict
        
        
listOfPossibilities = getNumberOfPossibilitiesForAllNodes(adapters)
combinations = getNumberOfCombinationsFor(listOfPossibilities)
# print(adapters)
print("Day 10 - part two: the total number of combinations is:", combinations[0])
