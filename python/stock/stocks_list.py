class StocksList:
    """
    A class representing a list of stocks and traders.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StocksList, cls).__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        """
        Initialize the StocksList object.
        """
        self.traders = []
        self.stocks = {
            "ABC": 100.0,
            "XYZ": 50.0
        }

    def register_trader(self, trader):
        """
        Register a trader with the StocksList.
        """
        self.traders.append(trader)

    def update_price(self, stock, price):
        """
        Update the price of a stock and notify traders.
        """
        self.stocks[stock] = price
        self.notify_traders(stock, price)

    def notify_traders(self, stock, price):
        """
        Notify all registered traders about the stock price update.
        """
        for trader in self.traders:
            trader.update(stock, price)
