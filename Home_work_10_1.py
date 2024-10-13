# Home Work 10.1

def pow(x):
    return x ** 2

def some_gen(begin, end, func):

    element_of_sequence = begin
    for elements in range(end):
        yield element_of_sequence
        element_of_sequence = func(element_of_sequence)


from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')