print('Current entrys')
D={'Peter':0, 'Julien':0, 'Jonas':0}
c=None
c2=None
c3=None
#Display current databank
print(D)

# add entries
while c != 'n':
    A=float(input('What do you want to do? 1=add entrys, 2=delete entrys, 3=change balance'))
    if A == 1:
        print('Please enter a new customer and balance in this order.')
        customer=input()
        balance=input()
        D[customer]=balance
        print(D)
#delete entries
    elif A==2:
        print('What entrys do you want to delete?')
        print('You can stop with the deletion at any start of the cycle with typing "n"')
        print(D)
        while c2 != 'n':
            d=input()
            del D[d]
            print(D)
            c=input('Do you want to delete another entry? y/n')
#change balance
    elif A==3:
        while c3 != 'n':
            print('Whos customers balance do you want to change?')
            print(D)
            B=input()
            Amount=D[B]
            print(f'The current Balance of {B} is {Amount}')
            B2 = input('What amount do you want to deposit or retrive?' + '\t' +
                       'Please enter the amount and a minus sign if you want to retrive or a plus to deposit.')
            if type(B2)== str:
                print('This is text. Do not be silly.')
                continue
            B3=D[B] + float(B2)
            if B3 < 0:
                print('You cannot retrieve more than you have.')
                continue
            elif B3 > 0:
                D[B]=B3
                print(f'The new balance of {B} is {D[B]}')
            else:
                print('This input is not valid. Please try again!')
                continue
            c3=input('Do you want to make another balance change? y/n')
    else: print('This is no valid input')
    c=input('Do you want to continue? y/n')
