string=str(input())

def check(string):
    brackets = ['()', '{}', '[]']
    while any(x in string for x in brackets):
        for x in brackets:
            string = string.replace(x, '')
    return not string

print("Balanced" if check(string) else "Unbalanced")

