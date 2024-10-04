
from python.utils.payment import Payment


class UPIPayment(Payment):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        # Logic for paying via UPI can go here
        print(f"Paid {amount} via UPI ({self.upi_id})")

    def copy(self):
        return UPIPayment(self.upi_id)

    def set_upi_id(self, upi_id):
        self.upi_id = upi_id
