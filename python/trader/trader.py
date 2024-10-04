from abc import ABC, abstractmethod

class Trader(ABC):
    """
    A base class for traders.
    """

    @abstractmethod
    def update(self, stock, price):
        """
        Update the stock price for the trader.
        """
        pass


