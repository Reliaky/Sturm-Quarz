import random
tuple_list = []
for i in range(10):
    tuple = random.randrange(1, 100), random.randrange(1, 100), random.randrange(1, 100)
    tuple_list.append(tuple)
print(tuple_list)

def nr3(tup):
    return tup[2]

tuple_list.sort(key=nr3)
print(tuple_list)
