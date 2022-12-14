x = int(input("Write x here: "))
n = int(input("Write n here: "))

def xpowerofn(x,n):
    if n == 1:
        return x
    if n == 0:
        return 1
    else:
        return x**n

print(xpowerofn(x,n))
