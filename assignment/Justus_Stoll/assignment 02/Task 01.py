print('Please type something.')
word = input()
letter = ''
length = 0
x = 0
word_control = ''

while word_control != word:
    letter = str(word[x])
    length = length + 1
    word_control = word_control + letter
    x = x + 1

print(length)
