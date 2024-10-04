from abc import ABC, abstractmethod
from python.account.account import Account

class Transaction(ABC):
    """
    An abstract base class representing a Transaction.
    """

    @abstractmethod
    def execute(self, account: Account, amount: float):
        """
        Execute the transaction on the given account with the specified amount.
        """
        pass
