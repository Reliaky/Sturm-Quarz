print('Please provide a mathematical expression.')
expression = str(input())
opened = 0
closed = 0
symbol = ''
correctness = 'correct'
for x in range(len(expression)):
    symbol = expression[x]
    if symbol == '(':
        opened = opened + 1
    if symbol == ')':
        closed = closed + 1
    if closed > opened:
        correctness = 'incorrect'
        print('Your input is incorrect.')
        break
if correctness == 'correct':
    print('Your input is correct.')
