from Seat import *

# reading and prearing data
data = open("seating-system-test.txt", "r").read().splitlines()

seats = []
for rowIdx, line in enumerate(data):
    row = []
    for colIdx, char in enumerate(line):
        if(char == '.'):
            row.append(None) # not a seat
        else:
            row.append(Seat(char, rowIdx, colIdx))
    seats.append(row)

def printSeats(matrix):
    for row in matrix:
        line = ""
        for seat in row:
            if(seat is None):
                line += ". "
            else:
                line += seat.__str__() + " "
        print(line)

def calculateNextIteration(matrix):
    stable = True
    for row in matrix:
        for seat in row:
            if(seat is not None):
                if(seat.canBeOccupied(matrix, 5)):
                    if(not seat.isOccupied()):
                        stable = False
                    seat.occupy()
                else:
                    if(seat.isOccupied()):
                        stable = False
                    seat.empty()
    return matrix, stable

def findNumberOfOccupiedSeats(matrix):
    stable = False
    numberOfOccupiedSeats = 0
    iterations = 0
    while(not stable):
        matrix, stable = calculateNextIteration(matrix)
        iterations += 1
    for row in matrix:
        for seat in row:
            if(seat is not None and seat.isOccupied()):
                numberOfOccupiedSeats += 1
    return matrix, iterations, numberOfOccupiedSeats

# print("========================= START ================================")
# printSeats(seats)
# print("========================= FIRST ITERATION ================================")
# seats, stable = calculateNextIteration(seats)
# print(f'stable: {stable}')
# printSeats(seats)
# print("========================= SECOND ITERATION ================================")
# seats, stable = calculateNextIteration(seats)
# print(f'stable: {stable}')
# printSeats(seats)
# print("========================= THIRD ITERATION ================================")
# seats, stable = calculateNextIteration(seats)
# print(f'stable: {stable}')
# printSeats(seats)
# print("========================= FOURTH ITERATION ================================")
# seats, stable = calculateNextIteration(seats)
# print(f'stable: {stable}')
# printSeats(seats)
# print("========================= FIFTH ITERATION ================================")
# seats, stable = calculateNextIteration(seats)
# print(f'stable: {stable}')
# printSeats(seats)
# print("========================= SIXTH ITERATION ================================")
# seats, stable = calculateNextIteration(seats)
# print(f'stable: {stable}')

print("========================= END - number of occupied seats: ================================")
seats, iterations, numberOfOccupiedSeats = findNumberOfOccupiedSeats(seats)
printSeats(seats)
print("seats occupied", numberOfOccupiedSeats)
print("iterations:", iterations)