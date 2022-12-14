import random
import itertools

N = 10
R = 100

res = random.sample(list(itertools.product(range(R + 1), repeat = 3)), N)

print("The N random tuples : " + str(res))
