print('Please provide a number!')
number = int(input())
na = 0
nb = 1
Fibo = na + nb
if number == 0:
    print(0)
if number >= 1:
    print(0)
    print(1)
while number >= Fibo:
    print(Fibo)
    na = nb
    nb = Fibo
    Fibo = na + nb

