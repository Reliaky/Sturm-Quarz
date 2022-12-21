class Customer:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(self.balance)

uwe = Customer(0)
uwe.deposit(20)
uwe.withdraw(10)
