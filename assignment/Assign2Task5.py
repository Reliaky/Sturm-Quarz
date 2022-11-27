x=str(input())
def check(x):
    stacking=[]
    for i in x:
        if i in "(":
            stacking.append(")")
        elif i in ")":
            if not stacking or i != stacking.pop():
                return "Unbalanced"
    if not stacking:
        return "Balanced"
    else:
        return "Unbalanced"

print(check(x))

