from BankAccountClass import BankAccount

konto = BankAccount(1000)
print(konto.balance)

konto.deposit(500)
print(konto)

konto.withdraw(400)
print(konto)