import math #подключил для использования поиска наименьщего общего кратного

class OperationsWithFractionsMixin:
    @staticmethod
    def sub(first_fraction, second_fraction):
        if first_fraction.denominator != second_fraction.denominator:
            denominator = (first_fraction.denominator * second_fraction.denominator) // math.gcd(first_fraction.denominator, second_fraction.denominator)
            self_factor = int(denominator / first_fraction.denominator)
            fraction_factor = int(denominator / second_fraction.denominator)
            numerator = (self_factor * first_fraction.numerator) - (fraction_factor * second_fraction.numerator)
        else:
            numerator = first_fraction.numerator - second_fraction.numerator
            denominator = first_fraction.denominator
        return Fraction(numerator, denominator)

    @staticmethod
    def add(first_fraction, second_fraction):
        if first_fraction.denominator != second_fraction.denominator:
            denominator = (first_fraction.denominator * second_fraction.denominator) // math.gcd(first_fraction.denominator, second_fraction.denominator)
            self_factor = int(denominator / first_fraction.denominator)
            fraction_factor = int(denominator / second_fraction.denominator)
            numerator = (self_factor * first_fraction.numerator) + (fraction_factor * second_fraction.numerator)
        else:
            numerator = first_fraction.numerator + second_fraction.numerator
            denominator = first_fraction.denominator
        return Fraction(numerator, denominator)

    @staticmethod
    def mul(first_fraction, second_fraction):
        numerator = first_fraction.numerator * second_fraction.numerator
        denominator = first_fraction.denominator * second_fraction.denominator
        return Fraction(numerator, denominator)

    @staticmethod
    def truediv(first_fraction, second_fraction):
        numerator = first_fraction.numerator * second_fraction.denominator
        denominator = first_fraction.denominator * second_fraction.numerator
        return Fraction(numerator, denominator)

class Fraction(OperationsWithFractionsMixin):
    def __init__(self, num, den):
        self.numerator = num
        self.denominator = den

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, numerator):
        self.__numerator = numerator

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator):
        assert denominator > 0, 'Знаменатель дроби может быть больше 0' #будет "упрощенная" дробь, за знак дроби будет отвечать только числитель
        self.__denominator = denominator

    def __sub__(self, fraction):
        if self.denominator != fraction.denominator:
            denominator = (self.denominator * fraction.denominator) // math.gcd(self.denominator, fraction.denominator)
            self_factor = int(denominator / self.denominator)
            fraction_factor = int(denominator / fraction.denominator)
            numerator = (self_factor * self.numerator) - (fraction_factor * fraction.numerator)
        else:
            numerator = self.numerator - fraction.numerator
            denominator = self.denominator
        return Fraction(numerator, denominator)

    def __add__(self, fraction):
        if self.denominator != fraction.denominator:
            denominator = (self.denominator * fraction.denominator) // math.gcd(self.denominator, fraction.denominator)
            self_factor = int(denominator / self.denominator)
            fraction_factor = int(denominator / fraction.denominator)
            numerator = (self_factor * self.numerator) + (fraction_factor * fraction.numerator)
        else:
            numerator = self.numerator + fraction.numerator
            denominator = self.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, fraction):
        numerator = self.numerator * fraction.numerator
        denominator = self.denominator * fraction.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, fraction):
        numerator = self.numerator * fraction.denominator
        denominator = self.denominator * fraction.numerator
        return Fraction(numerator, denominator)

    @classmethod
    def object_from_string(cls, string_numerator_and_denominator):
        numerator_and_denominator = [int(iterator) for iterator in string_numerator_and_denominator.split('/')]
        return cls(*numerator_and_denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

numerator = 3
denominator = 5
string_numerator_and_denominator = '1/2'

first_fraction = Fraction(numerator, denominator)
print(f"{first_fraction} — работа __str__")

second_fraction = Fraction.object_from_string(string_numerator_and_denominator)
print(f"{second_fraction} — работа @classmethod\n")

print(f"{first_fraction - second_fraction} — работа __sub__")
print(f"{first_fraction + second_fraction} — работа __add__")
print(f"{first_fraction * second_fraction} — работа __mul__")
print(f"{first_fraction / second_fraction} — работа __truediv__\n")

print(f"{first_fraction.sub(first_fraction, second_fraction)} — работа sub")
print(f"{first_fraction.add(first_fraction, second_fraction)} — работа add")
print(f"{first_fraction.mul(first_fraction, second_fraction)} — работа mul")
print(f"{first_fraction.truediv(first_fraction, second_fraction)} — работа truediv")