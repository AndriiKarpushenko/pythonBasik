# Home_work_15_1

import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def find_pair_factors(self, product_number):
        best_pair = (1, product_number)
        for i in range(1, int(math.sqrt(product_number)) + 1):
            quotient_value, remainder_value = divmod(product_number, i)
            if remainder_value == 0:
                difference_value = abs(i - quotient_value)
                if difference_value < abs(best_pair[0] - best_pair[1]):
                    best_pair = (i, quotient_value)
        return best_pair

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        new_square = self.get_square() + other.get_square()
        width, height = self.find_pair_factors(new_square)
        return Rectangle(width, height)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented
        new_square = self.get_square() * n
        width, height = self.find_pair_factors(new_square)
        return Rectangle(width, height)

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() == other.get_square()

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, square={self.get_square()})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print("Ok")
