#input
decNum = input('Please Type your number: ')
floatDecNum = float(decNum)
#output
#print(oct(floatDecNum))
def DecimalToOctal(n):
    if(n > 0):
        # recursively calling on n/8
        DecimalToOctal(int(n/8))
        # printing the remainder
        print(n%8, end='')

DecimalToOctal(floatDecNum)
