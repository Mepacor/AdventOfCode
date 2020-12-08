# Policy class that can validate passwords
class Policy(object):
    def __init__(self, range, character):
        self.range = range
        self.character = character
    
    def getRange(self):
        return self.range
    
    def getCharacter(self):
        return self.character

class OldPolicy(Policy):
    def __init__(self, range, character):
        super().__init__(range, character)

    def isValidPassword(self, password):
        count = str(password).count(self.getCharacter())
        if (count >= int(self.getRange()[0]) and count <= int(self.getRange()[1])):
            return True
        else:
            return False

class NPTPolicy(Policy):
    def __init__(self, range, character):
        super().__init__(range, character)

    def getPosition(self, index):
        return int(self.getRange()[index])-1

    def isValidPassword(self, password):
        if (str(password)[self.getPosition(0)] == self.character and str(password)[self.getPosition(1)] != self.character):
            return True
        elif (str(password)[self.getPosition(0)] != self.character and str(password)[self.getPosition(1)] == self.character):
            return True
        else:
            return False