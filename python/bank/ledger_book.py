class LedgerBook:
    """
    A class representing a LedgerBook for an account.
    """

    def __init__(self, account_number):
        """
        Initialize the LedgerBook object with the given account number.
        """
        self.account_number = account_number
        self.amount = 0.0

    def update_ledger(self, amount, account_number):
        """
        Update the ledger with the given amount and account number.
        """
        # logic
        pass

    def get_balance(self):
        """
        Get the current balance in the ledger.
        """
        return self.amount

    def get_account_number(self):
        """
        Get the account number associated with the ledger.
        """
        return self.account_number
