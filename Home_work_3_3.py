# Home work 3.3

original_list = [1, 2, 3, 4, 5, 6]

if len(original_list) == 0:
    new_list = [[], []]
else:
    middle_list  = len(original_list ) // 2
    first_half = original_list[:middle_list + 1]
    second_half = original_list[middle_list + 1:]
    new_list  = [first_half, second_half]

print(new_list )