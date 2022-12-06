import random
numlist = []

for i in range(10):
    number = random.randrange(1, 100)
    numlist.append(number)
print(numlist)

maximum = numlist[0]
x = 0
for i in range(9):
    num = numlist[x+1]
    if num > maximum:
        maximum = num
    x = x + 1
print(maximum)


