# PassportScanner class that holds the required fields and checks if a Passport is valid or not
from Rule import *
from RuleMapper import *

class PassportScanner(object):
    def __init__(self, requiredFieldKeys):
        self.requiredFieldKeys = requiredFieldKeys
        self.RulesEnabled = False

    def withRulesEnabled(self):
        self.RulesEnabled = True
        return self

    def isValidScan(self, passport):
        index = 0
        isValidScan = True
        while(isValidScan and index < len(self.requiredFieldKeys)):
            fieldKey = self.requiredFieldKeys[index]
            if(fieldKey not in passport.getFields()):
                isValidScan = False
            elif(self.RulesEnabled): # only true for part 2
                isValidScan = RuleMapper.getRuleClass(fieldKey).validate(passport.getValueFor(fieldKey))
                #print("Rule validation check for", fieldKey, ":", isValidScan)
            index += 1
        return isValidScan

    

    