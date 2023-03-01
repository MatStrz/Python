from BankAccountClass import MinimumBalanceAccount


kontoMinimum = MinimumBalanceAccount(1000)

kontoMinimum.deposit(500)
result = kontoMinimum.try_withdraw(900)

print(result.message, result.amount)
