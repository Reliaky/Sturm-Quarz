#Fibonacci stuff
n=int(input("Enter numbers to display"))
Fib= [0,1]
F1= 0
F2= 1
a=1
while n!=2:
    if len(Fib)==2:
        m= F1 + F2
        Fib.append(m)
        n = n - 1
    else:
        F1= Fib[0+a]
        F2 = Fib[1+a]
        a = a + 1
        m = F1 + F2
        Fib.append(m)
        n=n-1
print(Fib)
