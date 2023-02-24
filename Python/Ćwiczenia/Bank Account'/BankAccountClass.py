
class BankAccount:
    nextId = 1

    def __init__(self, balance):
        self.Id = BankAccount.nextId
        BankAccount.nextId += 1
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def __str__(self):
        return str(self.balance)
