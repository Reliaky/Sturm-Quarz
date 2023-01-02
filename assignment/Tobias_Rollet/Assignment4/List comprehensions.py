
def remove_long_words():
    s=input('Please give me a sentence')
    n=int(input('Maximum word length'))
    string=str.split(s)
    [string.remove(x) for x in string if len(x) >= n]
    print(string)

remove_long_words()

