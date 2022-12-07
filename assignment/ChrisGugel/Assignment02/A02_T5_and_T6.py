# Task 05 & 06
def check(x):
    ob = tuple('({[')
    cb = tuple(')}]')
    n = dict(zip(ob, cb))
    q = []

    for i in x:
        if i in ob:
            q.append(n[i])
        elif i in cb:
            if not q or i != q.pop():
                return 'Incorrect input!'
    if not q:
        return 'Correct input!'
    else:
        return 'Incorrect input!'
