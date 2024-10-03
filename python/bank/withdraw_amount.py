from python.account.account import Account
from python.bank.transaction import Transaction

class WithdrawAmount(Transaction):
    """
    A concrete implementation of the Transaction interface.
    This transaction performs a deposit operation on the given account.
    """

    def execute(self, account: Account, amount: float):
        """
        Execute the transaction by depositing the specified amount into the account.
        """
        account.withdraw(amount)
