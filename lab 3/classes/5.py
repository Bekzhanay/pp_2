class Account:
    def __init__(self, balance):
        self.owner = input("Owner is: ")
        self.balance = balance
        print(f"The balance: {self.balance}")

    def deposit(self):
        print("Replenishment: ")
        self.balance = self.balance + int(input())
        return self.balance
        
    def withdraw(self):
        print("Transfer: ")
        self.balance = self.balance - int(input())
        return self.balance

pr = Account(100)
print(f"Your balance: {pr.withdraw()}")
print(f"Your balance: {pr.deposit()}")
print(f"Your balance: {pr.withdraw()}")