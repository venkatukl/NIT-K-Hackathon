from python.account.account import Account
from python.bank.transaction import Transaction

class TxnManager:
    """
    A class representing a Transaction Manager.
    """

    def __init__(self):
        """
        Initialize the TxnManager object.
        """
        self.transaction = None

    def set_transaction(self, transaction: Transaction):
        """
        Set the transaction to be executed.
        """
        self.transaction = transaction

    def execute_transaction(self, account: Account, amount: float):
        """
        Execute the transaction on the given account with the specified amount.
        """
        if self.transaction:
            self.transaction.execute(account, amount)
        else:
            raise ValueError("No transaction set")
