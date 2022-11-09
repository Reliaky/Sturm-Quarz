print('Please insert 3 lengths of the triangle sides: ')
numberX = input('length number 1: ')
numberY = input('length number 2: ')
numberZ = input('length number 3: ')

#input string to integer
x = int(numberX)
y = int(numberY)
z = int(numberZ)

if z < (x + y):
    print('This is a valid input')
    if x == y and y == z:
        print('The Triangle is equilateral.')
    else:
        if x == y or y == z or x == z:
            print('The Triangle is isosceles.')
        else:
            print('The triangle is scalene.')
else:
    print('No valid input, try again!')
