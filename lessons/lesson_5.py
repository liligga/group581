# Dunder methods - magic methods - double underscore
from lessons.lesson_1 import Car

class Money:
    def __init__(self, amount=0):
        self.amount = amount

    def __str__(self):
        return f"экземпляр Money: {self.amount}"

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.amount - other.amount)

    def __mul__(self, other):
        pass

    def __eq__(self, other):
        # return self.amount == other.amount
        if self.amount == other.amount:
            return True
        else:
            return False

    # gt - greater than - self > other
    # ge - greater than or equal: self >= other
    # lt - less than: self < other
    # le - less than or equal: self <=  other
    def __gt__(self, other):
        if self.amount > other.amount:
            return True
        else:
            return False

igor_money = Money(100)
print(igor_money)
adilet_money = Money(200)
total_money = igor_money + adilet_money
print(total_money)
print(igor_money == adilet_money)
print(total_money > igor_money)

my_car = Car(color="red", model="Honda")
print(my_car)