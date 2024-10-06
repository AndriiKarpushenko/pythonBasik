# Home work 9.2.

def difference(*args):
    if len(args) == 0:
        return 0

    maximum_value_of_argument = max(args)
    minimum_value_of_argument = min(args)

    result_calculation = round(maximum_value_of_argument - minimum_value_of_argument, 2)

    return result_calculation


print(difference(1, 2, 3))  # Виведе 2
print(difference(5, -5))  # Виведе 10
print(difference(10.2, -2.2, 0, 1.1, 0.5))  # Виведе 12.4
print(difference())  # Виведе 0
