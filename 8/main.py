import numpy as np
import time
from Instruction import *

boot = open("boot-code.txt", "r").read().splitlines()

# Part 1: calculating the value in the accumulator before infinite loop
start = time.time()
instructionsVisited = np.zeros(len(boot)) # booltable that keeps track of instruction was
it = 0 # iterator
acc = 0 # accumulator
while(it < len(boot) and not(instructionsVisited[it])):
    instruction = Instruction(boot[it].split(" "))
    instructionsVisited[it] = 1
    it, acc = instruction.execute(it, acc)
end = time.time()


print("Day 8 - part one: the accumulator state before the infinite loop is:", acc)
print("     Time needed in seconds:", end-start)


# Part 2: fix the infinite loop and calculate the value in the accumulator
# in part one: we know that the corrupted instruction must be located in one of the visited instructions (1 in bool table)
# so we can narrow our search down to those instructions
start = time.time()
corruptCandidates = instructionsVisited
bootSuccess = False
corruptIt = 0 # iterator to loop over the corruptCandidates, every loop, we try to swap 1 operation only and see if the boot succeeds
while(corruptIt < len(boot) and not(bootSuccess)):
    if(corruptCandidates[corruptIt]):
        it = 0 # iterator
        acc = 0 # accumulator
        instructionsVisited = np.zeros(len(boot))
        while(it < len(boot)):
            if( not(instructionsVisited[it]) ):
                instructionsVisited[it] = 1
                instruction = Instruction(boot[it].split(" "))
                if(it == corruptIt): # swap the operation of the current possible corrupted candidate
                    #print("swapping: ", boot[it])
                    instruction.swapOperation()
                it, acc = instruction.execute(it, acc)
            else:
                #print("not the right candidate")
                break
        bootSuccess = it >= len(boot)
        #print("success:", bootSuccess)
    corruptIt += 1
end = time.time()

print("\nDay 8 - part two: the accumulator state after fixing the boot code is:", acc)
print("     Corrupted instruction:", boot[corruptIt-1], ", at index:", corruptIt-1)
print("     Time needed in seconds:", end-start)