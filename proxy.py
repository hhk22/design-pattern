
# Proxy Pattern
# Real객체에 직접 접근하는 대신, Proxy 객체가 이를 대신한다. 

class Card:
    def __init__(self) -> None:
        self.card_number: str = None
        self.cash = 0

    def set_card_number(self, number):
        self.card_number = number

    def increase_cash(self, amount):
        self.cash += amount


class CardProxy:
    def __init__(self):
        self._card = Card()

    def set_card_number(self, number: int):
        # ex) ######## -> ####-####
        if len(number) != 8:
            raise ValueError('The length of the number should be 8')

        card_string = str(number)
        self._card.set_card_number(card_string[:4] + '-' + card_string[4:])
        print(self._card.card_number)

    def increase_cash(self, amount):
        if amount > 0 and self._card.card_number is not None:
            self._card.increase_cash(amount)
            print(self._card.cash)


card = CardProxy()
card.set_card_number('81239034')
