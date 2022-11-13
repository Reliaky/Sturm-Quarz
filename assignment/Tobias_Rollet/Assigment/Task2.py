word= input("please enter a Word")
#set word length
n= len(word)-1
Backwords =[]

# with a loop structure

while n != -1:
    Backwords.append(word[n])
    n=n-1

Full_Backwords ="".join(Backwords)
print(Full_Backwords)

#Now with only array indexes
print(word[::-1])



