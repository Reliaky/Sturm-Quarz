print("Please provide the costumers' names separated with a comma.")
customers = input()
customers_list = customers.split(', ')
balances = {str(customer): 0 for customer in customers_list}
print(balances)

print("Do you want to add or remove customers? If so, please answer with 'Yes'")
answer1 = input()
if answer1 == 'Yes':
    print("Please provide the names of one / multiple new customers or one / multiple customers you want to remove.")
    names = input()
    names_list = names.split(', ')
    for name in names_list:
        if name in balances:
            del balances[name]
        else:
            balances[name] = 0
    print(balances)
else:
    print("No customers are added or removed.")

def deposit(customer, amount):
    if customer not in balances:
        print("The costumer's name is invalid.")
    elif amount < 0:
        print("The amount is invalid.")
    else:
        balances[customer] = balances[customer] + amount
    print(balances)

def withdraw(customer, amount):
    if customer not in balances:
        print("The costumer's name is invalid.")
    elif amount < 0:
        print("The amount is invalid.")
    else:
        balances[customer] = balances[customer] - amount
        if balances[customer] < 0:
            print("This action is invalid because of overdrawing the account.")
            balances[customer] = balances[customer] + amount
    print(balances)

while True:
    print("If you want to deposit money, please type 'd'. If you want to withdraw money, please type 'w'.")
    answer2 = input()
    if answer2 == 'd':
        print("Please type in the customer, confirm with enter and type in the amount to be deposited.")
        deposit(input(), int(input()))
    if answer2 == 'w':
        print("Please type in the customer, confirm with enter and type in the amount to be withdrawn.")
        withdraw(input(), int(input()))
    if answer2 == 'b':
        break
