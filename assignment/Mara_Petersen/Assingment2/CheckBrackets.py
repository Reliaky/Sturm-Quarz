
brackets = input("Write your Formula here: ")

# Python3 code to Check for
# balanced parentheses in an expression
open_list = ["[","{","("]
close_list = ["]","}",")"]

# Function to check parentheses
def check(brackets):
	stack = []
	for i in brackets:
		if i in open_list:
			stack.append(i)
		elif i in close_list:
			pos = close_list.index(i)
			if ((len(stack) > 0) and
				(open_list[pos] == stack[len(stack)-1])):
				stack.pop()
			else:
				return "Incorrect"
	if len(stack) == 0:
		return "Correct"
	else:
		return "Incorrect"

print(brackets,"-",check(brackets))
