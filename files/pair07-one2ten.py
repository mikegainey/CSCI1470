# read space-separated numbers in one2ten.txt and print a running sum

f = open("one2ten.txt")
numbers = f.read().split()
f.close()

runningSum = 0
for number in numbers:
    print("+ {} = ".format(number), end='')
    runningSum += int(number)
    print(runningSum)
