
from python.account.account import Account


class Current(Account):
    """
    A concrete implementation of Account for Current account.
    """
    
    def deposit(self, amount):
        """
        To deposit a specified amount into the current account
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        To withdraw a specified amount from the current account
        """
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def get_balance(self):
        """
        Method to get the current account balance
        """
        return self.balance

    def get_account_number(self):
        """
        Method to get the current account number
        """
        return self.account_number