# Task 3
word = input('Enter word here! -> ')
word = word.replace(' ', '')
word_dict = {}

for i in word:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1

print(str(word_dict))
