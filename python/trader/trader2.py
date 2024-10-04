
from python.trader.trader import Trader


class Trader2(Trader):
    """
    A trader that updates the stock price.
    """

    def update(self, stock, price):
        """
        Update the stock price for the trader.
        """
        print(f"Trader 2 updated {stock} to {price}")