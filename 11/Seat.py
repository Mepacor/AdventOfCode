# Seat class that holds the status of occupancy
class Seat(object):
    def __init__(self, occupancy, rowNumber, colNumber):
        self.warm = False # stupid workaround to check if the seat was previously occupied or not, because copying the global seats matrix still uses the same object references.
        self.occupancy = occupancy
        self.rowNumber = rowNumber
        self.colNumber = colNumber

    def isOccupied(self):
        return self.occupancy == '#'
    
    def isEmpty(self):
        return self.occupancy == 'L'

    def isWarm(self):
        return self.warm

    def occupy(self):
        if(self.occupancy == 'L'):
            self.warm = False
        else:
            self.warm = True
        self.occupancy = '#'
    
    def empty(self):
        if(self.occupancy == '#'):
            self.warm = True
        else:
            self.warm = False
        self.occupancy = 'L'

    #TODO use limitToFirstNeighbor so that part 1 and part 2 can work separatly
    def isSideOccupiedFor(self, seats, side, limitToFirstNeighbor=False):
        rowMove = side[0]
        colMove = side[1]
        sideInString = [["top left", "top", "top right"], ["left", "middle", "right"], ["bottom left", "bottom", "bottom right"]]
        occupied = False

        nextRow = self.rowNumber + rowMove
        nextCol = self.colNumber + colMove
        while(nextRow >= 0 and nextRow < len(seats) and nextCol >= 0 and nextCol < len(seats[0])):
            if(self.loggingEnabled()):
                print("len", len(seats[0])-1)
                print("moving " + sideInString[rowMove+1][colMove+1])
            seat = seats[nextRow][nextCol]
            if(seat is None):
                nextRow += rowMove
                nextCol += colMove
            elif (rowMove > 0 or (rowMove == 0 and colMove > 0)): # going down or right must use isOccupied
                occupied |= seat.isOccupied()
                break
            else:
                occupied |= seat.isWarm()
                break
        
        return occupied

    def loggingEnabled(self):
        return False #self.rowNumber == 0 and self.colNumber == 8

    # seats that are already modified, must be checked with their isWarm() method, because.. references!
    # ugly method, but too far in and too lazy to refactor
    def canBeOccupied(self, seats, maxOccupied): 
        count = 0
        rowIdx = self.rowNumber
        colIdx = self.colNumber
            
        if(rowIdx > 0):                       # top neighbor
            if (self.isSideOccupiedFor(seats, [-1,0])):
                count = count + 1 
        if(colIdx > 0):                       # left neigbor
            if (self.isSideOccupiedFor(seats, [0,-1])):
                count = count + 1 
        if(rowIdx < len(seats)-1):           # bottom neighbor
            if (self.isSideOccupiedFor(seats, [+1,0])):
                count = count + 1 
        if(colIdx < len(seats[0])-1):           # right neighbor
            if (self.isSideOccupiedFor(seats, [0,+1])):
                count = count + 1 

        if(rowIdx > 0 and colIdx > 0):                           # top left neighbor
            if (self.isSideOccupiedFor(seats, [-1,-1])):
                count = count + 1
        if(rowIdx < len(seats)-1 and colIdx < len(seats[0])-1):   # bottom right neighbor
            if (self.isSideOccupiedFor(seats, [+1,+1])):
                count = count + 1
        if(rowIdx < len(seats)-1 and colIdx > 0):               # bottom left neighbor
            if (self.isSideOccupiedFor(seats, [+1,-1])):
                count = count + 1
        if(rowIdx > 0 and colIdx < len(seats[0])-1):               # top right neighbor
            if (self.isSideOccupiedFor(seats, [-1,+1])):
                count = count + 1

        if(self.loggingEnabled()):
            print(f"count: {count}")
        
        if(self.isOccupied()):
            return count < maxOccupied
        else:
            return count == 0

    def __str__(self):
        # return "Occupied seat" if self.isOccupied() else "Empty seat"
        return "#" if self.isOccupied() else "L"

    def __repr__(self):
        return self.__str__()