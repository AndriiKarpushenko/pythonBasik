# Home work 7.4

def common_elements( ):

    numbers_list_of_3 = list(range(0, 101, 3))
    numbers_list_of_5 = list(range(0, 101, 5))

    numbers_set_of_3 = set(numbers_list_of_3)
    numbers_set_of_5 = set(numbers_list_of_5)

    intersection_set = numbers_set_of_3.intersection(numbers_set_of_5)

    return intersection_set


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')
