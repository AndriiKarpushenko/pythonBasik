# Home work 8.3

def find_unique_value(some_list):
    all_numbers_set = set(some_list)
    unique_numbers_set = all_numbers_set - (set(some_list[::2]) & set(some_list[1::2]))
    if len(unique_numbers_set) > 0:
        unique_number = list(unique_numbers_set)[0]
    else:
        None
    return unique_number


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
