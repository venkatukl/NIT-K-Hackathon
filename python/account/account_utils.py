
from python.account.current import Current
from python.account.savings import Savings


def get_account(account_type, account_number):
    """
    Create and return an account based on the given account type
    """
    if account_type.lower() == "savings":
        return Savings(account_number)
    elif account_type.lower() == "current":
        return Current(account_number)
    else:
        raise ValueError("Invalid account type")