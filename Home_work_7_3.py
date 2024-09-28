# Home work 7.3

def second_index(text, some_str):
    first_find = text.find(some_str)
    if first_find == -1:
        return None
    second_find = text.find(some_str, first_find + len(some_str))
    if second_find == -1:
        return None
    return second_find


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')