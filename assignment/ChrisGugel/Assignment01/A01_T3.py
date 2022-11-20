# Task 03
print("Input number for Fibonacci-sequencing!")
n = int(input())

a = 0
b = 1
x = a + b

if n == 0:
    print(0)

if n >= 1:
    print(0)
    print(1)

while n >= x:
    print(x)
    a = b
    b = x
    x = a + b

print("done")
