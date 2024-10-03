
from python.account.account import Account


class Savings(Account):
    """
    A concrete implementation of Account for Savings account.
    """

    def deposit(self, amount):
        """
        To deposit a specified amount into the savings account
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        To withdraw a specified amount from the savings account
        """
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def get_balance(self):
        """
        Method to get the savings account balance
        """
        return self.balance

    def get_account_number(self):
        """
        Method to get the savings account number
        """
        return self.account_number