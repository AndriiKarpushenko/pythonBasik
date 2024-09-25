# Home work 6.1

import string

input_string = input("Enter two letters separated by a dash: ")
parts_string = input_string.split('-')
char_before_dash = parts_string[0]
char_after_dash = parts_string[1]

all_char_string = string.ascii_letters

left_part_string = all_char_string.index(char_before_dash)
right_part_string = all_char_string.index(char_after_dash)

all_char_input_string = all_char_string[left_part_string:right_part_string + 1]

print(all_char_input_string)
