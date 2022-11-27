import random
randomlist=[]
def rlist(x):
    for i in x:
        n=random.randrange(1, 100, 1)
        randomlist.append(n)
    return randomlist
y=rlist(range(10))
print(y)

def maxnum(y):
    maximum=100
    for i in range(100):
        maximum -= 1
        if maximum in y:
            return maximum
print(maxnum(y))





