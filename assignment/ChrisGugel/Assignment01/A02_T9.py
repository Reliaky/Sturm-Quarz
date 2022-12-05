# Task 09
import math

n = int(input('Enter number to approximate!'))


def euler(n):
    x = 2
    a = 0
    for i in range(0, n):
        a += x**i/math.factorial(i)

    return a


print(euler(n))
