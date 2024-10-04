
from python.trader.trader import Trader
from python.trader.trader_parent import TraderParent


class NotifyTraders(TraderParent):
    """
    A trader that notifies the update of the stock price.
    """

    def __init__(self, trader: Trader):
        """
        Initialize the NotifyTraders instance with a trader instance.
        """
        super(NotifyTraders, self).__init__(trader)

    def update(self, stock, price):
        """
        Update the stock price for the trader and notify the update.
        """
        super(NotifyTraders, self).update(stock, price)
        self.notify_update(stock, price)

    def notify_update(self, stock, price):
        """
        Notify the update of the stock price.
        """
        print(f"Trader {self.trader.__class__.__name__} updated {stock} to {price}")