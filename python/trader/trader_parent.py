
from python.trader.trader import Trader


class TraderParent(Trader):
    """
    A trader that delegates the update method to a trader instance.
    """

    def __init__(self, trader: Trader):
        """
        Initialize the TraderParent instance with a trader instance.
        """
        self.trader = trader

    def update(self, stock, price):
        """
        Update the stock price for the trader.
        """
        self.trader.update(stock, price)