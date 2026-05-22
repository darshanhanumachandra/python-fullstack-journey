from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount
    
    @abstractmethod
    def process(self):
        pass

class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number
    
    def process(self):
        print(f"Processing ${self.amount} with credit card {self.card_number}")
        print("✓ Payment successful via Credit Card")

class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email
    
    def process(self):
        print(f"Processing ${self.amount} with PayPal account {self.email}")
        print("✓ Payment successful via PayPal")

# Usage
card_payment = CreditCardPayment(100, "1234-5678-9012-3456")
paypal_payment = PayPalPayment(50, "user@gmail.com")

card_payment.process()
paypal_payment.process()

# The magic loop
print("\n--- Processing Multiple Payments ---")
payments = [card_payment, paypal_payment]
for payment in payments:
    payment.process()