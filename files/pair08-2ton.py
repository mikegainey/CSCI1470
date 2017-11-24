# user inputs a number, n
# program writes numbers 2 to n to a file (2-to-n.txt)

n = int(input("Enter an integer greater than 2: "))

# because range doesn't include the endpoint
if n % 2 == 0:
    n += 1


f = open("2-to-n.txt", 'w')

for number in range(2, n, 2):
    f.write(str(number) + ' ')
f.write('\n')

f.close()
