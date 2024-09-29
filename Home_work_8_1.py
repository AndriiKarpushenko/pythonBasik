def add_one(some_list):
    number = 0
    for digit in some_list:
        number = number * 10 + digit

    number += 1

    def converting_number_to_list(number):
        list_of_numbers = []
        for digit in str(number):
            list_of_numbers.append(int(digit))
        return list_of_numbers

    return converting_number_to_list(number)


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")