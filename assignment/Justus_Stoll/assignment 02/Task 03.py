print('Please provide a string.')
word = input()
no_spaces = ''.join(word.split())
occurrence = {no_spaces[x]: no_spaces.count(no_spaces[x]) for x in range(len(no_spaces))}
print(occurrence)
