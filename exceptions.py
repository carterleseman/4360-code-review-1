class BankingException(Exception):
    pass

class InsufficientFundsException(BankingException):
    def __str__(self):
        return "An error occurred: Insufficient Funds"

class InvalidAccountNumberException(BankingException):
    def __str__(self):
        return "An error occurred: Invalid Account Number"