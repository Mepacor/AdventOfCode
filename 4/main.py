from Passport import *
from PassportScanner import *
from Rule import *
from RuleMapper import *
# Reading and prepping the passport file 
batch = open("batch-file.txt", "r").read().splitlines()
fields = {}
passports = []
for line in batch:
    if(not len(line) == 0):
        fieldList = line.split(" ")
        for field in fieldList:
            key = field.split(":")[0]
            value = field.split(":")[1]
            fields[key] = value
    else:
        passports.append(Passport(fields.copy())) # use copy for different object reference
        fields.clear()
# print(passports[-1].getFields())

requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] # "cid" is made optional ;)
passportScanner = PassportScanner(requiredFields)

#-----------------------------------------------------------------------------------------------#
# Part 1: calculate the valid passports
validPassportCount = 0
for passport in passports:
    if(passportScanner.isValidScan(passport)):
        #print("Valid passport: ", passport.getFields())
        validPassportCount += 1
    else:
        #print("Invalid passport: ", passport.getFields())
        pass

print("Part 1: Out of", len(passports), "passwords:", validPassportCount, "passports are valid")

#-----------------------------------------------------------------------------------------------#
# Part 2: adding data validation rules
passportScanner = passportScanner.withRulesEnabled()
validPassportCount = 0
for passport in passports:
    if(passportScanner.isValidScan(passport)):
        validPassportCount += 1
    else:
        pass

print("Part 2: Out of", len(passports), "passwords:", validPassportCount, "passports are valid")
