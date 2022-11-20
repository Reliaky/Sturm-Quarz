# Task 04
print("Enter number!")

n = int(input())
ref_n = 0

if n >= 0:
    print(0)
while n >= ref_n:
    if (ref_n/3) == (float(ref_n//3)):
        ref_n += 1
        continue
    else:
        print(ref_n)
        ref_n += 1
