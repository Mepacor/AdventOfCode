
# Reading data and defining general functions
boardingPasses = open("boarding-seats.txt", 'r').read().splitlines()

def binToDec(string):
    result = 0
    for index, char in enumerate(string):
        result += toBit(char) * (2 ** (len(string)-index-1))
    return result

def toBit(char):
    if(char == "B" or char == "R"):
        return 1
    elif(char == "F" or char == "L"):
        return 0

# Part 1: find the highest seat ID
maxSeatId = -1
for boardingPass in boardingPasses:
    seatId = binToDec(boardingPass)
    if(maxSeatId < seatId):
        maxSeatId = seatId
print("Day 5 - Part one: highest seat id is", maxSeatId)

# Part 2: finding our seat ID
seatIds = []
for boardingPass in boardingPasses:
    seatIds.append(binToDec(boardingPass))
seatIds = sorted(seatIds)

ourSeatId = -1
index = 0
while(ourSeatId < 0 and index < len(seatIds)-1):
    index += 1
    seatId = seatIds[index]
    previousSeatId = seatIds[index-1]
    nextSeatId = seatIds[index+1]
    if( (previousSeatId + nextSeatId) % seatId == 1):
        ourSeatId = seatId + 1

print("Day 5 - Part two: our seat id is", ourSeatId)