#number of user
number = input('My number is: ')
intNumber = int(number)
i = 0
f0 = 0
f1 = 1

#print Fibonacci Numbers
print('The Fibonacci numbers are: ', '', end='')
while i < intNumber:
    print(f0, end='')
    Next = f0 + f1
    f0 = f1
    f1 = Next
    i = i + 1




