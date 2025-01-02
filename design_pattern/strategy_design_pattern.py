from abc import ABC , abstractmethod

#Abstract Class
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self , amount):
        pass

#Concrete Classes
class PaypalPaymentStrategy(PaymentStrategy):
    def pay(self , amount):
        print(f"Paid {amount} using Paypal")


class BitcoinPaymentStrategy(PaymentStrategy):
    def pay(self , amount):
        print(f"Paid {amount} using Bitcoin")


class CreditCardPaymentStrategy(PaymentStrategy):
    def pay(self , amount):
        print(f"Paid {amount} using Credit Card")



class ShoppingCart:
    def __init__(self , payment_method: PaymentStrategy):
        self.payment_method = payment_method
        def checkout(self , amount):
            return self.payment_method.pay(amount)
    

if __name__ == '__main__':
    
