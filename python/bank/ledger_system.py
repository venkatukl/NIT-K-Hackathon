from python.account.account import Account
from python.bank.ledger_book import LedgerBook

class LedgerSystem(Account):
    """
    A class representing a LedgerSystem that implements the Account interface.
    """

    def __init__(self, ledger_book: LedgerBook):
        """
        Initialize the LedgerSystem object with a LedgerBook instance.
        """
        self.ledger_book = ledger_book

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        """
        self.ledger_book.update_ledger(amount, "DEPOSIT")

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account.
        """
        self.ledger_book.update_ledger(-amount, "WITHDRAWAL")

    def get_balance(self) -> float:
        """
        Get the current balance of the account.
        """
        return self.ledger_book.get_balance()

    def get_account_number(self) -> str:
        """
        Get the account number associated with the account.
        """
        return "LEDGER"
