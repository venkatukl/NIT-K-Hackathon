# cart.py
class Cart:
    def __init__(self, payment_manager):
        self.payment_manager = payment_manager

    def checkout(self, amount):
        self.payment_manager.pay(amount)
