
from python.account.account import Account


class NewAccount(Account):
    """
    A class representing a New Account.
    Provides methods to manage the account balances.
    """

    def __init__(self):
        """
        Initialize the New Account object
        """
        self.accounts = []

    def __init__(self, accounts):
        """
        Initialize the New Account object
        """
        self.accounts = accounts

    def add_account(self, account):
        """
        Add an account to the New Account
        """
        self.accounts.append(account)

    def get_account_number(self):
        """
        Get the account number of the New Account
        """
        return "New-Acct-Num"

    def deposit(self, amount):
        """
        Deposit a specified amount to all accounts
        """
        for account in self.accounts:
            account.deposit(amount)

    def withdraw(self, amount):
        """
        Withdraw a specified amount from all accounts
        """
        for account in self.accounts:
            account.withdraw(amount)

    def get_balance(self):
        """
        Get the total balance of all accounts
        """
        balance = 0
        for account in self.accounts:
            balance += account.get_balance()
        return balance