from python.account.account import Account
from python.bank.deposit_amount import DepositAmount
from python.bank.test_bank import TestBank
from python.bank.withdraw_amount import WithdrawAmount

class TestBankManager:
    """
    A class representing a TestBankManager.
    """

    def __init__(self, bank: TestBank):
        """
        Initialize the TestBankManager object with a TestBank instance.
        """
        self.bank = bank

    def deposit_account(self, account: Account, amount: float):
        """
        Deposit an amount into an account.
        """
        self.bank.add_transaction(account, amount, DepositAmount())

    def withdraw_account(self, account: Account, amount: float):
        """
        Withdraw an amount from an account.
        """
        self.bank.add_transaction(account, amount, WithdrawAmount())

    def get_balance(self, account: Account):
        """
        Get the balance of an account.
        """
        self.bank.get_balance(account)
