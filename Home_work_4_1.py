# Home work 4.1

original_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

non_zero_elements_list = []
for elements in original_list:
    if elements != 0:
        non_zero_elements_list.append(elements)

zero_count = original_list.count(0)
new_list = non_zero_elements_list + [0] * zero_count

print(original_list)
print(new_list)