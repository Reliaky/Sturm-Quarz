x = str(input())
x=x.replace(" ", "")
def check_freq(x):
    freq = {}
    for i in set(x):
       freq[i] = x.count(i)
    return freq
print(check_freq(x))
