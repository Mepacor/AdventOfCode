# RuleMapper class that maps a field (String) to a Rule subclass for right validation
from Rule import *

class RuleMapper(object):
    
    ruleMap = {
        "byr": YearRule(1920, 2002),
        "iyr": YearRule(2010, 2020),
        "eyr": YearRule(2020, 2030),
        "hgt": HeightRule([150,193], [59,76]),
        "hcl": ColorRule("hcl", "^#([a-f]|[0-9]){6}$"),
        "ecl": ColorRule("ecl", ""),
        "pid": IdRule("^[0-9]{9}$")
    }

    @staticmethod
    def getRuleClass(fieldName):
        return RuleMapper.ruleMap[fieldName]