import random
randomlist = []
for i in range (0,10):
    n = random.randint(0,100)
    randomlist.append(n)
print("This is the random list: ", randomlist)

randomlist.sort()
print("The largest element is: ", randomlist[-1])
