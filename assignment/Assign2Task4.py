import numpy as np
import random

tuplelist=[]
for i in range(10):
    x=np.random.randint(1, 100, size=3)
    y=tuple(x)
    tuplelist.append(y)
print(tuplelist)

def third(num):
    return num[2]
sorted_list = sorted(tuplelist, key=third)
print(sorted_list)


