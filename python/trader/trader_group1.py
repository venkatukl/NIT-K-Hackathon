

from python.trader.trader import Trader


class TraderGroup1(Trader):
    """
    A trader that updates the stock price.
    """
    def update(self, stock, price):
        """
        Update the stock price for the trainer.
        """
        print(f"TraderGroup1 updated {stock} to {price}")