#Decimal to octal conversion

n = int(input("Please enter a non-negative number"))
if n < 0:
    print("This number is negative! Please try again")
    quit()
else:
    n=oct(n)
    print(n)

#a

#n = float(input("Please enter a non-negative number"))
#if n < 0:
#    print("This number is negative! Please try again")
#    quit()
#else:
#    n=oct(n)
#    print(n)