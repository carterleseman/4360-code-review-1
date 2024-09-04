from message import Message
from exceptions import BankingException, InvalidAccountNumberException

class User:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts
        self.message = Message()

    def show_accounts(self):
        self.message.print("{:<20}{:<0}".format("Account Number", "Amount"))
        for account_number, account in self.accounts.items():
            balance = account.check_balance()
            self.message.print("{:<20}{:<0}".format(account_number, balance))
 
    def deposit(self, args):
        try:
            account_number = int(args[0])
            amount = int(args[1])
            account = self.accounts.get(account_number)
            
            if not account:
                raise InvalidAccountNumberException

            account.deposit(amount)
            return account.check_balance()
        except BankingException as e:
            self.message.print(str(e))
        except Exception as e:
            self.message.print(f"An error occurred: {e}")

    def withdraw(self, args):
        try:
            account_number = int(args[0])
            amount = int(args[1])
            account = self.accounts.get(account_number)

            if not account:
                raise InvalidAccountNumberException

            account.withdraw(amount)
            return account.check_balance()
        except BankingException as e:
            self.message.print(str(e))
        except Exception as e:
            self.message.print(f"An error occurred: {e}")

    def transfer(self, args):
        try:
            from_account = int(args[0])
            to_account = int(args[1])
            amount = int(args[2])

            account1 = self.accounts.get(from_account)
            account2 = self.accounts.get(to_account)

            if not account1 or not account2:
                raise InvalidAccountNumberException

            account1.withdraw(amount)
            account2.deposit(amount)
        except BankingException as e:
            self.message.print(str(e))
        except Exception as e:
            self.message.print(f"An error occured: {e}")