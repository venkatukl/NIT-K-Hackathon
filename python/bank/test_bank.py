from python.account.account import Account
from python.bank.control_panel import ControlPanel
from python.bank.transaction import Transaction
from python.utils.notification import Notification

class TestBank:
    """
    A class representing a TestBank.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TestBank, cls).__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        """
        Initialize the TestBank object.
        """
        self.accounts = []
        self.notify_list = []
        self.control_panel = ControlPanel(self)

    def add_account(self, account: Account):
        """
        Add an account to the TestBank.
        """
        self.accounts.append(account)

    def add_transaction(self, account: Account, amount: float, txn: Transaction):
        """
        Add a transaction to the TestBank.
        """
        if self.control_panel.allow_request():
            try:
                txn.execute(account, amount)
                self.send_message(account)
                self.control_panel.record_success()
            except Exception as e:
                self.control_panel.record_failure()
                print(f"Transaction failed: {e}")
        else:
            print("Transaction rejected")

    def add_notification(self, notification: Notification):
        """
        Add a notification to the TestBank.
        """
        self.notify_list.append(notification)

    def remove_notification(self, notification: Notification):
        """
        Remove a notification from the TestBank.
        """
        self.notify_list.remove(notification)

    def send_notification(self, message: str):
        """
        Send a notification to all registered notifications.
        """
        for notification in self.notify_list:
            notification.send(message)

    def get_balance(self, account: Account) -> float:
        """
        Get the balance of an account.
        """
        return account.get_balance()

    def send_message(self, account: Account):
        """
        Send a message about the updated balance of an account.
        """
        self.send_notification(f"Balance updated for account {account.get_account_number()}: ${account.get_balance()}")

    def send_messages(self):
        """
        Send messages about the updated balance of all accounts.
        """
        for account in self.accounts:
            self.send_message(account)
