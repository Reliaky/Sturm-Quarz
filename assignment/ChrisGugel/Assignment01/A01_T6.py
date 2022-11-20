print("Enter number!")

n = int(input())
octa = ''

while True:
    if n // 8 == 0:
        octa = octa + str(n % 8)
        break
    octa = octa + str(n % 8)
    n = n % 8

print(octa[::-1])
