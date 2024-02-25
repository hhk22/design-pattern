# proxy vs facade
# proxy는 실제 객체와 동일한 작용을하는 대리 객체를 제공. 
# facade는 복잡한 sub-system에 대해서 단순한 interface를 제공. 
from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


# Real Subject
class Bank(Payment):
    def __init__(self):
        self.card_number = None

    def set_card(self, card_number):
        self.card_number = card_number
    
    def do_pay(self):
        if self.card_number:
            print("Bank:: Paying...")
            return True
        return False

# Proxy
class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()
    
    def do_pay(self):
        card_number = input("insert card_number")
        self.bank.set_card(card_number)
        return self.bank.do_pay()


class You:
    def __init__(self):
        self.debit_card = DebitCard()
        self.is_purchased = None
    
    def make_payment(self):
        self.is_purchased = self.debit_card.do_pay()
    

you = You()
you.make_payment()
