x=int(input("Give a value for side x"))
y=int(input("Give a value for side y"))
z=int(input("Give a value for side z"))
if z == x+y or z > x +y:
    print("This input does not work")
    quit()

elif z< x+y:
    
    if x == y and y ==z:
        print("this is a equilateral triangle")
    if (x == y and y != z) or (z == y and z != x):
        print("this is a isosceles triangle")
    if x != y and x != z and z != y:
        print("this is another triangle")