from exceptions import InsufficientFundsException

class Account:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            raise InsufficientFundsException
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount
        return self.balance