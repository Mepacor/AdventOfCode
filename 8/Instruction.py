# instruction class that holds the current instruction
class Instruction(object):
    def __init__(self, instruction):
        self.operation = instruction[0]
        self.value = int(instruction[1])

    def execute(self, it, acc):
        if(self.operation == "nop"):
            it += 1
        if(self.operation == "acc"):
            acc += self.value
            it += 1
        if(self.operation == "jmp"):
            it += self.value
        return it, acc
    
    def isAccInstruction(self):
        return self.operation == "acc"
    
    def isJmpInstruction(self):
        return self.operation == "jmp"

    def swapOperation(self):
        if(self.operation == "jmp"):
            self.operation = "nop"
        elif(self.operation == "nop"):
            self.operation = "jmp"
        else:
            #print("i am a ACC, i cannot swap")
            pass

