from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
    @abstractmethod
    def refund(self, amount):
        pass


class CreditCardPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата картой: {amount} руб.")
    
    def refund(self, amount):
        print(f"Возврат на карту: {amount} руб.")


class PayPalPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата через PayPal: {amount} руб.")
    
    def refund(self, amount):
        print(f"Возврат через PayPal: {amount} руб.")


if __name__ == "__main__":
    try:
        payment = PaymentSystem()
    except TypeError as e:
        print(f"Невозможно создать PaymentSystem: {e}")
    
    print()

    card = CreditCardPayment()
    card.pay(1000)
    card.refund(500)
    
    print()
    
    paypal = PayPalPayment()
    paypal.pay(2000)
    paypal.refund(1000)