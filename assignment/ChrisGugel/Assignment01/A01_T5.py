#Task 05
while True:
        print("Enter the three sidelengths of triangle!")

        x = int(input())
        y = int(input())
        z = int(input())

        if z > x + y or x > y + z or y > x + z:
                print("Invalid entries! Please enter valid lengths!")
                continue

        if x == y == z:
                print("Equilateral triangle!")
                break

        elif x == y or x == z or y == z:
                print("Isosceles triangle!")
                break

        else:
                print("Scalene triangle!")
                break
