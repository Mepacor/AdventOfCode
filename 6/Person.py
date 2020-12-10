# class Person that holds the answers of that person
class Person(object):
    def __init__(self, setOfAnswers):
        self.setOfAnswers = setOfAnswers

    def getAnswers(self):
        return self.setOfAnswers