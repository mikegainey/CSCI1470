print()

for a in range(1,11):
    print("{:2}s:".format(a), end=' ')
    for b in range(1,11):
        print("{:3}".format(a * b), end=' ')
    print()

print()
