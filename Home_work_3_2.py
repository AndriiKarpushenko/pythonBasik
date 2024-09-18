# Home work 3.2

lst_first = [12, 3, 4, 10]
if len(lst_first ) > 1:
    last_element = lst_first [-1]
    lst_first .insert(0, last_element)
    del lst_first [-1]
print(lst_first)

lst_second = [12, 3, 4, 10, 8]
if len(lst_second) > 1:
    last_element = lst_second[-1]
    lst_second.insert(0, last_element)
    lst_second.pop()
print(lst_second)

lst_third = [1]
if len(lst_third) > 1:
    last_element = lst_third[-1]
    lst_third.insert(0, last_element)
    lst_third.pop()
print(lst_third)

lst_fourth = [ ]
if len(lst_fourth ) > 1:
    last_element = lst_fourth [-1]
    lst_fourth .insert(0, last_element)
    del lst_fourth [-1]
print(lst_fourth)
