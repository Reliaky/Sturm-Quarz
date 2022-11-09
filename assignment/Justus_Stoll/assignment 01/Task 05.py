print('Please give the length of the sides of the triangle and confirm each length with enter.')
a = int(input())
b = int(input())
c = int(input())

if (a > (b + c)) or (b > (a + c)) or (c > (a + b)):
    print('That is not a triangle.')
elif a == b == c:
    print('The triangle is equilateral.')
elif a == b or a == c or b == c:
    print('The triangle is isosceles.')
else:
    print('The triangle is scalene.')
