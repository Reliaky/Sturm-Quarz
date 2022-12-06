print('Who wants to queue? Please give the names separated by a comma.')
names = str(input())
queue = names.split(', ')
print('The queue is: ' + str(queue))
while queue != []:
    print('Please type "Next" if it is the next persons turn or add other persons to the queue.')
    command = input()
    if command == 'Next':
        print("It's "+ str(queue[0]) + "'s turn.")
        del(queue[0])
        print('The queue is: ' + str(queue))
    else:
        queue.append(command)
        print('The queue is: ' + str(queue))

