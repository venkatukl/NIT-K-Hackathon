
from python.trader.trader import Trader
from python.trader.trader_parent import TraderParent


class LogTraders(TraderParent):
    """
    A trader that logs the update of the stock price.
    """

    def __init__(self, trader: Trader):
        """
        Initialize the LogTraders instance with a trader instance.
        """
        super(LogTraders, self).__init__(trader)

    def update(self, stock, price):
        """
        Update the stock price for the trader and log the update.
        """
        super(LogTraders, self).update(stock, price)
        self.log_update(stock, price)

    def log_update(self, stock, price):
        """
        Log the update of the stock price.
        """
        print(f"Trader {self.trader.__class__.__name__} updated {stock} to {price}")
