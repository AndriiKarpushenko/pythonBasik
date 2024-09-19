# Home work 3.3

original_list = [1, 2, 3, 4, 5, 6]

if len(original_list) == 0:
    new_list = [[], []]
else:
    middle_list  = len(original_list ) // 2
    first_new_list = original_list[:middle_list + 1]
    second_new_list = original_list[middle_list + 1:]
    new_list  = [first_new_list, second_new_list]

print(new_list)
