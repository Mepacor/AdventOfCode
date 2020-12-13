import re
import time

bagRules = open("bag-rules-test.txt", "r").read().splitlines()
#bagRules = open("bag-rules-test.txt", "r").read().splitlines()

# Part 1: calculate the gold bag thing recursively
# deleting the value in the list in an attempt to improve efficiency results in corrupt indexing, and is therefore dangerous
# using bool table made performance worse
counter = 0
def recursiveSearch(bagType, count):
    pattern = re.compile("^(?!(" + bagType + ")).*" + bagType)
    for index,rule in enumerate(bagRules):
        if(pattern.match(rule) is not None):
            newBagType = ' '.join(rule.split(" ")[0:2])
            #print(newBagType)
            count = recursiveSearch(newBagType, count) + 1
    return count

start = time.time()
counter = recursiveSearch("shiny gold", counter)
end = time.time()
print("Day 7 - part one: The amount of bag colors that can eventually contain at least one shiny gold bag is", counter)
print("time elapsed in seconds:", end-start)

# Part 2: calculate the amount of individual bags are required inside our single shiny gold bag
# the recursive search was improved a lot by using a dict that holds the bagType as key, and the required amount of bags inside as value
# avg time of function without dict: 0.01299905776977539 seconds 
# avg time of function without dict: 0.00501806831359863 seconds
bagTypeDict = {}
def requiredRecursiveSearch(bagType):
    if bagType in bagTypeDict:
        return bagTypeDict[bagType]
    else:
        count = 1
        pattern = re.compile("^(" + bagType + ")")
        for index, rule in enumerate(bagRules):
            if(pattern.match(rule) is not None):
                dissectedRule = rule.split(',')
                for bagComposition in dissectedRule:
                    split = bagComposition.split(" ")
                    print(dissectedRule)
                    if(split[-3] != "no"):
                        count += ( int(split[-4]) * requiredRecursiveSearch(" ".join(split[-3:-1])) )
        bagTypeDict[bagType] = count
        return count

start = time.time()
counter = requiredRecursiveSearch("shiny gold")
end = time.time()
print("Day 7 - part two: the amount of individual bags that are required inside our single shiny gold bag is", counter-1)
print("time elapsed in seconds:", end-start)




