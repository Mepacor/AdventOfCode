data = open("XMAS.txt", "r").read().splitlines()
data = [int(i) for i in data] # convert to int

preambleSize = 25
preamble = data[0:preambleSize]

# Part 1: find the invalid number in the data
def isSumOfTwoNumbersIn(preamb, number):
    answer = 0
    for i in range(0, len(preamb)-1):
        if(answer == 0):
            for j in range(i+1, len(preamb)):
                if(preamb[i] + preamb[j] == number):
                    #print("numbers are: ", preamb[i], preamb[j])
                    answer = preamb[i] * preamb[j]
                    break
        else:
            break
    return answer != 0

def getInvalidNumberIn(data, preamb):
    result = -1
    for index in range(len(preamb), len(data)):
        if(isSumOfTwoNumbersIn(preamb, data[index])):
            preamb[index % len(preamb)] = data[index]
        else:
            result = data[index]
            break
    return result

invalidNumber = getInvalidNumberIn(data, preamble)
print("Day 9 - part one: Number that is not a sum of two other numbers in given preamble:", invalidNumber)


# Part 2: find the encryption weakness in the XMAS encoded data
# find a contiguous set of at least two numbers that are, summed up, equal to the invalid number
numbers = []
for i in range(0, len(data)-1):
    numbers.clear()
    numbers.append(int(data[i]))
    for j in range(i+1, len(data)):
        numbers.append(int(data[j]))
        if(sum(numbers) >= invalidNumber):
            break
    if(sum(numbers) == invalidNumber):
        break

print("Day 9 - part two: contiguous set of at least two numbers that are, summed up, equal to the invalid number:", numbers)
print("Lowest and higest number summed up, gives the answer:", min(numbers)+max(numbers))
