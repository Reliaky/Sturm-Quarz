import math

def decimal2binary(n):
    # function to convert decimal integers to binary
    x = []
    if n == 0:
       x = [0]
    while n > 0:
            x.append(n % 2)
            n = math.floor(n/2)
    if n < 0:
        print(bin(~n))
    return x[::-1]


