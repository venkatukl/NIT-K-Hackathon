
from python.utils.payment import Payment
from python.utils.payment_gateway import PaymentGateway


class NetBankingPayment(Payment):
    def __init__(self, gateway_name, account_number):
        self.gateway_name = gateway_name
        self.account_number = account_number
        self.payment_gateway = None

    def pay(self, amount):
        if self.payment_gateway is None:
            self.payment_gateway = PaymentGateway(self.gateway_name, self.account_number)
        self.payment_gateway.pay(amount)
        print(f"Paid {amount} via Net Banking")

    def copy(self):
        return self.copy(self) 
