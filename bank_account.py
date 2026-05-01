class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number=account_number
        self.balance=balance
    
    def deposit(self, amount): 
        self.balance+=amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            return -1
        else: 
            self.balance-=amount
            return 0
    
    def __str__(self):
        return f"Account Number: **{str(self.account_number)[-2:]}\nCurrent Balance: {self.balance:.2f}"
    

account = BankAccount(1234, 100.0)
print(account)
# Account Number: **34
# Current Balance: 100.00
account.deposit(50.0)
result = account.withdraw(120.0)
print("Withdrawal status:", "Success" if result == 0 else "Failed")
# Withdrawal status: Success
result = account.withdraw(50.0)
print("Withdrawal status:", "Success" if result == 0 else "Failed")
# Withdrawal status: Failed