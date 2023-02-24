from result import Ok, Error


class BankAccount:
    nextId = 1

    def __init__(self, balance):
        self.Id = BankAccount.nextId
        BankAccount.nextId += 1
        self.balance = balance

    def deposit(self, amount):
        """hear money checking if its real"""
        self.balance += amount

    def try_withdraw(self, amount):
        """ check if there is enough money, and withdraw"""
        if self.balance >= amount:
            self.balance -= amount
            return Ok("Withdrawing", amount)

        return Error('Not enough balance', amount)

    def __str__(self):
        return str(self.balance)


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, miniumBalance=1000):
        self.minimumBalance = miniumBalance
        super().__init__(balance)

    def try_withdraw(self, amount):
        if (self.balance - amount) > self.minimumBalance:
            return super().try_withdraw(amount)

        return Error('transaction denied:\nMinimum balance error', amount)
