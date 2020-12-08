# my first OOP python code ever written
from Policy import *
from Password import Password 

# reading and prepping data
report = open("password_list.txt", 'r')
data = report.read().splitlines()

policies = []
passwords = []
for line in data:
    policy = line.split(":")[0]
    password = line.split(":")[1].strip()
    policies.append(Policy(policy.split(" ")[0].split("-"), policy.split(" ")[1]))
    passwords.append(Password(password))

[print("-", end="") for x in range(0, 100)], print("")

# Part 1: Calculating number of valid passwords
validPasswordCount = 0
for index, password in enumerate(passwords):
    policies[index].__class__ = OldPolicy
    if(policies[index].isValidPassword(password.getPassword())):
        validPasswordCount += 1

print("Day 2 - part one:")
print("Total amount of passwords: ", len(passwords))
print("Amount of passwords that are valid: ", validPasswordCount)
print("Amount of invalid passwords: ", len(passwords) - validPasswordCount)

[print("-", end="") for x in range(0, 100)], print("")

# Part 2: Calculating number of valid passwords
validPasswordCount = 0
for index, password in enumerate(passwords):
    policies[index].__class__ = NPTPolicy
    if(policies[index].isValidPassword(password.getPassword())):
        validPasswordCount += 1

print("Day 2 - part two:")
print("Total amount of passwords: ", len(passwords))
print("Amount of passwords that are valid: ", validPasswordCount)
print("Amount of invalid passwords: ", len(passwords) - validPasswordCount)