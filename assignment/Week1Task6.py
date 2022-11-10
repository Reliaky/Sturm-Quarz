n = int(input())

i = 0
octal = []
while n!=0:
    rem = n%8
    octal.insert(i, rem)
    i = i+1
    n = int(n/8)

i = i-1
while i>=0:
    print(octal[i], end="")
    i = i-1
print()


