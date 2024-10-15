# Home Work 11.2

def generate_cube_numbers(end):

    cubes_of_numbers = (number ** 3 for number in range(2, end))

    for cube in cubes_of_numbers:
        if cube >= end:
            return
        yield cube


from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'Test1'
assert list(generate_cube_numbers(100)) == [8, 27, 64], 'Test2'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729], 'Test3'
print('Ok')
