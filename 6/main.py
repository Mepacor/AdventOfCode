from Group import *
from Person import *

formAnswers = open("form-answers.txt", "r").read().splitlines()

setOfAnswers = set()
listOfPersons = list()
listOfGroups = list()
for line in formAnswers:
    if(len(line) != 0):
        for answer in line:
            setOfAnswers.add(answer)
        listOfPersons.append(Person(setOfAnswers.copy()))
        setOfAnswers.clear()
    else:
        listOfGroups.append(Group(listOfPersons.copy()))
        listOfPersons.clear()

# Part 1: For each group, count the number of questions to which anyone answered "yes"
yesCounter = 0
for group in listOfGroups:
    yesCounter += len(group.getUnionAnswers())

print("Day 6 - part one: For each group, the total number count of questions to which ANYONE answered 'yes' is", yesCounter)

# Part 2: For each group, count the number of questions to which anyone answered "yes"
yesCounter = 0
for group in listOfGroups:
    yesCounter += len(group.getIntersectionAnswers())

print("Day 6 - part two: For each group, the total number count of questions to which EVERYONE answered 'yes' is", yesCounter)
