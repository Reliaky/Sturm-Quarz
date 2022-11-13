List=[]
m=int(input("Enter numbers to display"))
for n in range(0,m):
    if n ==0:
        print(n)
        List.append(n)
        continue
    d= n%3
    if d == 0:        
        continue
        #print(n, 'is divisable by 3')
    else:
        #print(n, 'is not divisable by 3')
        List.append(n)
print(List)






