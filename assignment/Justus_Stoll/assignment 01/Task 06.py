print('Please provide a number!')
number = int(input())
oct = ''

while True:
    if number // 8 == 0:
        oct = oct + str(number % 8)
        break
    oct = oct + str(number % 8)
    number = number // 8
print(oct[::-1])
