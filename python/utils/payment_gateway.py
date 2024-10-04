
class PaymentGateway:
    def __init__(self, gateway_name, account_number):
        self.gateway_name = gateway_name
        self.account_number = account_number

    def pay(self, amount):
        print(f"Paid {amount} via Gateway ({self.gateway_name}): Account Number - {self.account_number}")
