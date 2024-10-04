# payment_processor.py
class PaymentProcessor:
    def process_payment(self, type, amount):
        payment_channel = None
        
        if type == "credit":
            print("Processing credit payment for amount", amount)
            payment_channel = self._process_credit_payment(amount)
        elif type == "debit":
            print("Processing debit payment for amount", amount)
            payment_channel = self._process_debit_payment(amount)
        elif type == "netbanking":
            print("Processing netbanking payment for amount", amount)
            payment_channel = self._process_netbanking_payment(amount)
        elif type == "upi":
            print("Processing UPI payment for amount", amount)
            payment_channel = self._process_upi_payment(amount)
        else:
            print("Unknown Payment option")

        payment_channel.pay(amount)

    def _process_credit_payment(self, amount):
        return self._create_payment_object("1234-5678-9012-3456", "12/24", "123", amount)

    def _process_debit_payment(self, amount):
        return self._create_payment_object("9876-5421-8524-6523", "11/25", "893", amount)

    def _process_netbanking_payment(self, amount):
        return self._create_payment_object("HDFC", "1234567890", amount)

    def _process_upi_payment(self, amount):
        payment_channel = self._create_upi_payment_object(amount)
        new_payment = payment_channel.copy()
        new_payment.upi_id = "dummy@upi"
        new_payment.pay(amount * 0.02)
        return new_payment

    @staticmethod
    def _create_payment_object(card_number, expiration_date, cvv, amount):
        # For this example, we'll use an anonymous class to create a payment object.
        # In a real application, you would create a class for this type of object.
        return type('Payment', (), {
            'card_number': card_number,
            'expiration_date': expiration_date,
            'cvv': cvv,
            'amount': amount,
            'pay': lambda self: print("Payment of", self.amount, "made"),
            'copy': lambda self: type('Payment', (), {
                'card_number': self.card_number,
                'expiration_date': self.expiration_date,
                'cvv': self.cvv,
                'amount': self.amount
                }
            )
        })

    @staticmethod
    def _create_upi_payment_object(amount):
        return type('UPayment', (), {
            'upi_id': "customer@upi",
            'amount': amount,
            'pay': lambda self: print("Payment of", self.amount, "made"),
            'copy': lambda self: type('UPayment', (), {
                'upi_id': self.upi_id,
                'amount': self.amount
                }
            )
        })
