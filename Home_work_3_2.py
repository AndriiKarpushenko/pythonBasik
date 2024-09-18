# Home work 3.2

first_lst = [12, 3, 4, 10]
if len(first_lst) > 1:
    last_element = first_lst [-1]
    first_lst .insert(0, last_element)
    del first_lst [-1]
print(first_lst)

second_lst = [12, 3, 4, 10, 8]
if len(second_lst) > 1:
    last_element = second_lst[-1]
    second_lst.insert(0, last_element)
    second_lst.pop()
print(second_lst)

third_lst = [1]
if len(third_lst) > 1:
    last_element = third_lst[-1]
    third_lst.insert(0, last_element)
    third_lst.pop()
print(third_lst)

fourth_lst = [ ]
if len(fourth_lst) > 1:
    last_element = fourth_lst [-1]
    fourth_lst .insert(0, last_element)
    del fourth_lst [-1]
print(fourth_lst)
