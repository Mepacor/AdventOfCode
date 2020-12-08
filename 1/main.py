
# Reading and prepping data
report = open("expense_report.txt", 'r')
data = report.readlines()

numbers = []
for number in data:
    numbers.append(int(number))
# print(len(numbers))

# Part 1: O(N*(N-1)/2)
answer = 0
count = 0
for i in range(0, len(numbers)-1):
    if(answer == 0):
        for j in range(i+1, len(numbers)):
            count+=1
            if(numbers[i] + numbers[j] == 2020):
                print("numbers are: ", numbers[i], numbers[j])
                answer = numbers[i] * numbers[j]
                break
    else:
        break

print("Day one - part 1: Answer is \""+ str(answer) +"\". Found in " + str(count) + " iterations")

# Part 2: O(N*(N-1)(N-2)/4)
answer = 0
count = 0
i = 0
while answer == 0 and i < len(numbers)-2:
    j = i + 1
    while answer == 0 and j < len(numbers)-1:
        k = j + 1
        while answer == 0 and k < len(numbers):
            count+=1
            if(numbers[i] + numbers[j] + numbers[k] == 2020):
                print("numbers are: ", numbers[i], numbers[j], numbers[k])
                answer = numbers[i] * numbers[j] * numbers[k]
            k+=1
        j+=1
    i+=1

print("Day one - part 2: Answer is \""+ str(answer) +"\". Found in " + str(count) + " iterations")