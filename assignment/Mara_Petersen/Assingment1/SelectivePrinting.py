#Ask for User Number and convert to integer
userNumber = input('Enter your number: ')
intUserNumber = int(userNumber)

print('Your number is bigger or equal to, without numbers divisible by 3: ', end='')

#loop with printing the numbers
while intUserNumber >= 0:
    if (intUserNumber%3==0):
        print()
    else:
        print(intUserNumber, ",", end="")
    intUserNumber = intUserNumber - 1
