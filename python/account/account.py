from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number):
        """
        Constructor for Account object
        """
        self.account_number = account_number
        self.balance = 0

    @abstractmethod
    def deposit(self, amount):
        """
        Method to deposit a specified amount to the account
        """
        pass

    @abstractmethod
    def withdraw(self, amount):
        """
        Method to withdraw a specified amount from the account
        """
        pass

    @abstractmethod
    def get_balance(self):
        """
        Method to get the account balance
        """
        pass

    @abstractmethod
    def get_account_number(self):
        """
        Method to get the account number
        """
        pass
