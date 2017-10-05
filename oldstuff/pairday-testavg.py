# The user inputs a series of grades (ending with -1)
# The program prints the average grade

totalpoints, numgrades = 0, 0

print("\nEnter grades to average:")
while True:
    grade = int(input("  Enter a grade (-1 to end): "))
    if grade == -1:
        break
    else:
        totalpoints += grade
        numgrades += 1

average = totalpoints / numgrades

print("=" * 30)
print("The average grade is {:.2f}".format(average))
print("=" * 30)
print()
