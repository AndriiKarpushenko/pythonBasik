# Home Work 11.1

def prime_generator(end):
    number = 2
    while number <= end:
        prime_number_test = number > 1 and (number == 2 or number % 2 != 0)
        if prime_number_test:
            for i in range(3, int(number**0.5) + 1, 2):
                if number % i == 0:
                    prime_number_test = False
                    break
        if prime_number_test:
            yield number
        number += 1


from inspect import isgenerator
gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
