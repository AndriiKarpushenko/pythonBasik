# Home work 3.2

first_lst = [12, 3, 4, 10]
if len(first_lst) > 1:
    last_element = first_lst [-1]
    first_lst .insert(0, last_element)
    del first_lst [-1]
print(first_lst)
