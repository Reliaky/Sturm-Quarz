#Lambda function

x=int(input('please enter the lower limit.'))
y=int(input('please enter the upper limit.'))

number=range(x,y)

lam=list(filter(lambda x: x % 2 ==0, number))

print(list(number))
print(lam)