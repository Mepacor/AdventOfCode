# Group class that stores all yes-answered questions
from Person import *

class Group(object):
    def __init__(self, listOfPersons):
        self.listOfPersons = listOfPersons

    def getUnionAnswers(self):
        unionAnswers = set()
        for person in self.listOfPersons:
            unionAnswers = unionAnswers.union(person.getAnswers())
        return unionAnswers

    def getIntersectionAnswers(self):
        intersetAnswers = self.listOfPersons[0].getAnswers()
        for i in range(1, len(self.listOfPersons)):
            intersetAnswers = intersetAnswers.intersection(self.listOfPersons[i].getAnswers())
        return intersetAnswers