print('Please provide a number!')
number = int(input())
listnumber = 0

if number >= 0:
    print(0)

while number >= listnumber:
    if (listnumber/3) == (float(listnumber//3)):
        listnumber = listnumber + 1
        continue
    else:
        print(listnumber)
        listnumber = listnumber + 1
