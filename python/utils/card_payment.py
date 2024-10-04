# card_payment.py
class CardPayment:
    def __init__(self, card_number, expiration_date, cvv, amount):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv
        self.amount = amount

    def pay(self):
        print(f"Card payment of {self.amount} made. Card Number: {self.card_number}, Expiration Date: {self.expiration_date}, CVV: {self.cvv}")

    def copy(self):
        return CardPayment(self.card_number, self.expiration_date, self.cvv, self.amount)
