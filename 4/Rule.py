# Rule class with different validation implementations depending on the field
import re

class Rule(object):
    def validate(self, value):
        print("no implementation specified!")
        return False

class YearRule(Rule):
    def __init__(self, min, max):
        self.min = min
        self.max = max
    
    def validate(self, value):
        #print("validating YearRule...")
        return self.min <= int(value) <= self.max

class HeightRule(Rule):
    def __init__(self, cmRange, inchRange):
        self.cmRange = cmRange
        self.inchRange = inchRange

    def validate(self, measure):
        #print("validating HeightRule...")
        metric = measure[-2:len(measure)]
        value = measure[0:-2]
        if(metric == "cm"):
            return self.cmRange[0] <= int(value) <= self.cmRange[1]
        elif(metric == 'in'):
            return self.inchRange[0] <= int(value) <= self.inchRange[1]
        return False

class ColorRule(Rule):
    def __init__(self, type, regex):
        self.type = type
        self.eyeColors = ["amb","blu","brn","gry","grn","hzl","oth"]
        self.pattern = re.compile(regex)

    def validate(self, value):
        if(self.type == "ecl"):
            return value in self.eyeColors
        elif(self.type == "hcl"):
            return self.pattern.match(value) is not None
        return False

class IdRule(Rule):
    def __init__(self, regex):
        self.type = type
        self.pattern = re.compile(regex)

    def validate(self, value):
        return self.pattern.match(value) is not None