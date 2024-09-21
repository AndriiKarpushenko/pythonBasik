# Home work 4.2

original_list = [0, 1, 7, 2, 4, 8]

even_index_elements = original_list[::2]

sum_even_index_elements = 0
for element in even_index_elements:
    sum_even_index_elements = sum_even_index_elements + element

if original_list:
    last_element = original_list [-1]
else:
    last_element = 0

result = sum_even_index_elements * last_element

print(original_list)
print(even_index_elements)
print("sum of elements =", sum_even_index_elements)
print("result =", result)